#!/usr/bin/python3

import socket

ip="127.0.0.1"
port=2222

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
	msg=input("enter msg-----> ")
	data=msg.encode('ascii')
	s.sendto(data,(ip,port))
	print(s.recvfrom(100))
