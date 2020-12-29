#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9090

serversocket.bind((host, port))

serversocket.listen(5)

while True:
    clientsocket, address = serversocket.accept()

    print("connection from {}".format(address))

    message = "connected to the server\r\n"
    clientsocket.send(message)

    clientsocket.close()
