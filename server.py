#server.py

from socket import *
import threading

BUFFERSIZE = 2048

serverPort = 1234

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))


#become a server socket
serverSocket.listen(5)

print "Server ready..."


#connection socket list
connectSocket_list = []

def broadcast(msg, clientSocket):
	for c in connectSocket_list:
		if msg == "QUIT":
			msg = "Client ", connectSocket_list.index(clientSocket), " has disconnected"
		c.send(msg)

def recv_msg(clientSocket):
	while True:
		msg = connectionSocket.recv(BUFFERSIZE)	
		msg = "Client " + str(connectSocket_list.index(clientSocket)) + ": " + msg
		print msg
		broadcast(msg, clientSocket)
		
		#end thread, close connection
		if msg == "QUIT":
			clientSocket.close()
			break


while True:
	connectionSocket, addr = serverSocket.accept()
	connectionSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
	connectSocket_list.append(connectionSocket)
	
	ct = threading.Thread(target=recv_msg, args=(connectionSocket, ))
	ct.start()
	

connectionSocket.close()

