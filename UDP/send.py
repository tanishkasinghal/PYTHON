#!/usr/bin/python3
#import lib
import socket
#target ip and port (use 0.0.0.0 for any connected ip--ec2instance)
ip="127.0.0.1"
port=2222
#create a udp socket
#              IP4(TCP--INET6)  udp(TCP--STREAM)
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


while True:
	msg=input("enter msg-----> ")
	data=msg.encode('ascii')
	s.sendto(data,(ip,port))
	print(s.recvfrom(100))
