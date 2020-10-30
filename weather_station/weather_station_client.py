# Weather station client
# Connects to a SUB socket on tcp://localhost:5556
# Reads weather updates from server and finds average for given postal code

import sys
import zmq

# Create SUB socket
context = zmq.Context()
socket = context.socket(zmq.SUB)

# Attache SUB socket to server
print("Subscribing to weather server updates: ")
socket.connect("tcp://localhost:5556")

# Filter updates pertaining to specified postal code, default is Little Rock, AR
postal_code_filter = sys.argv[1] if len(sys.argv) > 1 else "72204"

# Python 2 compatability
if isinstance(postal_code_filter, bytes):
	postal_code_filter = postal_code_filter.decode('ascii')
socket.setsockopt_string(zmq.SUBSCRIBE, postal_code_filter) # Only subscribe to updates that contain specified postal code

# Process 10 updates 
total_temp = 0

for update_nbr in range(10):
	string = socket.recv_string()
	postal_code, temperature, humidity = string.split()
	total_temp += int(temperature)

print("Average temperature for zipcode '%s' was %dF" % (
	postal_code_filter, total_temp / (update_nbr + 1))
)
