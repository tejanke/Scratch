#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

address = input("Enter IP to scan: ")
print(address)


scan = input("""
What scan do you want to run?
\t1) TCP Connect Scan
\t2) SYN Scan
\t3) UDP Scan
""")
print(scan)

if scan == '1':
    print("nmap version: {}".format(scanner.nmap_version()))
    scanner.scan(address, '400-500', '-v -sT')
    print(scanner.scaninfo())
    print(type(scanner.scaninfo()))
    print("IP {} is {}".format(address, scanner[address].state()))
    print(scanner[address].all_protocols())
    print("Open ports {}".format(scanner[address]['tcp'].keys()))
if scan == '2':
    print("nmap version: {}".format(scanner.nmap_version()))
    scanner.scan(address, '400-500', '-v -sS')
    print(scanner.scaninfo())
    print(type(scanner.scaninfo()))
    print("IP {} is {}".format(address, scanner[address].state()))
    print(scanner[address].all_protocols())
    print("Open ports {}".format(scanner[address]['tcp'].keys()))
if scan == '3':
    print("nmap version: {}".format(scanner.nmap_version()))
    scanner.scan(address, '400-500', '-v -sU')
    print(scanner.scaninfo())
    print(type(scanner.scaninfo()))
    print("IP {} is {}".format(address, scanner[address].state()))
    print(scanner[address].all_protocols())
    print("Open ports {}".format(scanner[address]['udp'].keys()))
else:
    print("{} is not an option".format(scan))
    exit