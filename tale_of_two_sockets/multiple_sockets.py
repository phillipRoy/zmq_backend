# Reading from multiple sockets
# Based on code by Jeremy Avnet (brainsik) spork(dash)zmq(at)theory(dot)org

import zmq, time

# Create ZeroMQ Context
context = zmq.Context()

# Connect to task ventilator
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# Connect to weather server
subscriber = context.socket(zmq.SUB)
subscriber.connect("tcp://localhost:5556")
subscriber.setsockopt(zmq.SUBSCRIBE, b"72204")

# Process messages from both sockets with priority to ventilator
while True:
	# Process waiting tasks
	while True:
		try:
			msg = receiver.recv(zmq.DONTWAIT)
		except zmq.Again:
			break
		# process task

	# Process any waiting weather updates
	while True:
		try: 
			msg = subscriber.recv(zmq.DONTWAIT)
		except zmq.Again:
			break
		# process weather update

	# wait if nothing to do
	time.sleep(0.001)