# Hello World zmq server
# Binds Response socket to port 5555 and waits for a message
# Will reply to client with b"World"

import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
	# wait for next request from client
	message = socket.recv()
	print("Received request: %s" % message)

	# Wait a second until reply to client
	time.sleep(1)

	# Send reply to client
	socket.send(b"World")
