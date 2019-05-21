#!/usr/bin/python3
# import lib
import socket
#target ip and port
ip="127.0.0.1"
port=2222
#create a udp socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#bind ip and port
s.bind((ip,port))
while True:
	msg=s.recvfrom(100)
	print(msg)
	data=input("reply: ")
	s.sendto(data.encode('ascii'),msg[1])
