# client.py

from socket import *
import threading
import sys, os

BUFFERSIZE = 2048

serverName = "127.0.0.1"
# serverName = "10.11.3.26"
serverPort = 1234

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print "Connected to server!"

#declare thread variables -- 
sendThread = None
recvThread = None

def recv_msg():
	while True:
		msg = clientSocket.recv(BUFFERSIZE)
		print msg
		if not msg: break

def send_msg():
	while True:
		msg = raw_input()
		clientSocket.send(msg)
		if msg == "QUIT":
			print "You have disconnected."
			clientSocket.close()
			os._exit(1)

		
sendThread = threading.Thread(target=send_msg)
sendThread.start()

recvThread = threading.Thread(target=recv_msg)
recvThread.start()
