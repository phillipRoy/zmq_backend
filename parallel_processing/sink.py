# Task sink
# Binds PULL socket to tcp://localhost:5558
# Collects results from workers via above socket
# 
# Based on code by Lev Givon <lev(at)columbia(dot)edu>

import zmq, time, sys

# Create ZMQ Context
context = zmq.Context()

# Create PULL socket for sink
receiver = context.socket(zmq.PULL)
receiver.bind("tcp://*:5558")

# Wait for start of batch
s = receiver.recv() # This statement is blocking and awaits ventilator to press "Enter"

# Start tracking time
tstart = time.time()

# Process 100 confirmations
for task_nbr in range(100):
	s = receiver.recv()
	if task_nbr % 10 == 0:
		sys.stdout.write(':')
	else:
		sys.stdout.write('.')
	sys.stdout.flush()

# Calculate and report duration of batch
tend = time.time()
print("Total elapsed time: %d msec" % ((tend-tstart) * 1000))