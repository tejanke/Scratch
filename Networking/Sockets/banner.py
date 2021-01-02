#!/usr/bin/python3

import socket

def banner(address, port):

    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.settimeout(5)
    clientsocket.connect((address, int(port)))

    print(clientsocket.recv(1024).decode('utf-8').rstrip())

def main():
    address = input("Enter IP: ")
    port = input("Enter port: ")
    banner(address, port)

main()
