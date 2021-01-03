#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.settimeout(3)

host = input("Enter IP: ")
port = int(input("Enter port: "))

def port_scanner(host, port):
    print("Scanning {}".format(host))
    if clientsocket.connect_ex((host, port)):
        print("Port {} is closed".format(port))
    else:
        print("Port {} is open".format(port))

port_scanner(host, port)
