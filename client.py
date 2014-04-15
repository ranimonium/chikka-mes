# client.py

from socket import *
import threading
import sys, os

BUFFERSIZE = 2048

serverName = "127.0.0.1"
# serverName = "10.11.3.26"
serverPort = 60007

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

print "Connected to server!"

#declare thread variables -- 
sendThread = None
recvThread = None

def recv_msg():
	try:
		while True:
			msg = clientSocket.recv(BUFFERSIZE)
			# print len(msg)
			if len(msg) == 0:
				raise KeyboardInterrupt
	except KeyboardInterrupt:
		os._exit(1)
		# sys.exit(1)

def send_msg():
	try:
		while True:
			msg = raw_input()
			clientSocket.send(msg)
			if "QUIT" in msg:
				print "You have disconnected."
				clientSocket.close()
				raise KeyboardInterrupt

	except KeyboardInterrupt:
		# os._exit(1)
		sys.exit(1)


		
sendThread = threading.Thread(target=send_msg)
sendThread.start()

recvThread = threading.Thread(target=recv_msg)
recvThread.start()
