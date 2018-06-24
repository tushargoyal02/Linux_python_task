#!/usr/bin/python2

#THIS PROGRAM IS FOR THE SERVER! HAVE A LOOK

#send Socket Creation
#importing socket library
import socket,sys

#AF_INET refers to addresss family of ipv4   and SOCK-DGRAM refers to UTP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#set IP adress as of server
ip="192.168.43.40"
port= 8888
TIMEOUT=100


s.bind((ip,port))
s.settimeout(TIMEOUT)

#while(4>2):
#	t= s.recvfrom(40)
#	print "rec from client" +t[0]
#	s.sendto("hello",t[1])

try :
	while True :
		#receiving the message from user in message variale		
		r = s.recvfrom(1000)
	#In line below [r] the r[0] contain the message while the r[1] contains the ip and port!
		print("receive from client : " + r[0])
	#replying to the user
		reply = raw_input('server : ')
		client_address = r[1]
		s.sendto(reply, client_address)
except:
	print("timeout or no server running")
