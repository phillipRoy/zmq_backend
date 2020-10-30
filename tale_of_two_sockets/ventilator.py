# Task Ventilator
# Bind PUSH socket to tcp://localhost:5557
# Send tasks to connected workers
# 
# Based on code by Lev Givon <lev(at)columbia(dot)edu>

import zmq, random, time

try:
	raw_input
# Exception for Python 3 compatability of user input
except NameError:
	raw_input = input

# Create ZMQ context
context = zmq.Context()

# Create ZMQ PUSH Socket for sender
sender = context.socket(zmq.PUSH)
sender.bind("tcp://*:5557")

# Create ZMQ PUSH Socket to access sink
sink = context.socket(zmq.PUSH)
sink.connect("tcp://localhost:5558")

print("Press Enter when workers are ready...")
_ = raw_input()
print("Sending tasks to workers...")

# Send signal for start of batch
sink.send(b'0')

# Init rng
random.seed()

# Send 100 tasks
total_msec = 0
for task_nbr in range(100):
	# Random workload from 1 to 100 miliseconds
	workload = random.randint(1, 100)
	total_msec += workload

	sender.send_string(u'%i' % workload) # u'' is unicode string, perhaps replace with b'' representation

print("Total expected cost: %s msec" % total_msec)

# Give ZMQ time to deliver
time.sleep(1)