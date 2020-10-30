# Weather Station Server
# Binds PUB socket to tcp://*:5556
# Publishes random weather data to subscribers

import zmq
from random import randrange

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:
    postal_code = randrange(1, 100000)
    temperature = randrange(-80, 135)
    humidity = randrange(10, 60)

    socket.send_string("%i %i %i" % (postal_code, temperature, humidity))
