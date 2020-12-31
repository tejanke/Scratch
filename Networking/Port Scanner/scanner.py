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