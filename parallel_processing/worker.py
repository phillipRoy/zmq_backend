# Task worker
# Connects a PULL socket to tcp://localhost:5557
# Gathers workloads from ventilator via above socket
# Connects a PUSH socket to tcp://localhost:5558
# Pushes results to task sink via above socket
# 
# Based on code by Lev Givon <lev(at)columbia(dot)edu>

import zmq, sys, time

# Create ZeroMQ Context
context = zmq.Context()

# Create PULL socket to ventilator
receiver = context.socket(zmq.PULL)
receiver.connect("tcp://localhost:5557")

# Socket to send messages to sink
sender = context.socket(zmq.PUSH)
sender.connect("tcp://localhost:5558")

# Process tasks forever
while True:
	s = receiver.recv()
	
	# Simple progress indicator for viewer
	sys.stdout.write('.')
	sys.stdout.flush()
	
	# Do the work
	time.sleep(int(s) * 0.001)
	
	# Send results to sink
	sender.send(b'')