# Hello World zmq client
# Connects Request socket tcp://localhost:5555
# Expects "World" from server

import zmq

context = zmq.Context()

# Create Socket to connect to server
print("Connecting to Hello World server...")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# Create 10 requests and wait for each response
for request in range(10):
    print("Sending request %s ..." % request)
    socket.send(b"Hello")

    # Get reply from server
    message = socket.recv()
    print("Received reply %s [ %s ]" % (request, message))
