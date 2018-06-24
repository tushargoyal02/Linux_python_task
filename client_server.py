#!/usr/bin/python2

#THIS PROGRAM IS FOR THE CLIENT USER!

#send Socket Creation
#importing socket library
import socket,sys

#AF_INET refers to addresss family of ipv4   and SOCK-DGRAM refers to UTP protocol
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


#set IP adress as of server
ip="192.168.43.40"
#SET port number as per your choice.
port=8888
TIMEOUT=100

s.settimeout(TIMEOUT)


try:
	while True:
		#takng the message from user in message variale		
		message = raw_input("Client : ")
		#using sendto function we are sending message to the server. 
		s.sendto(message,(ip,port))
	#ip and port of server ecvform function client are reciverd with 	
	#using recvform function we are receiving message from the client
		t= s.recvfrom(1000)
		print("Receive from Server: " +t[0])
		user=raw_input("Do you want to quit : Y/N")
		#If user type(Y) then exit with connection from the user.	
		if user == 'Y' :
			s.sendto("Client has Quit : Please exit",(ip,port))
			exit()
except:
	print("Timeout or No client running")	
