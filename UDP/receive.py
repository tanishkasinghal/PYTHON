#!/usr/bin/python3

import socket

ip="127.0.0.1"
port=2222

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind((ip,port))
while True:
	msg=s.recvfrom(100)
	print(msg)
	data=input("reply: ")
	s.sendto(data.encode('ascii'),msg[1])
