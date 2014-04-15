#server.py

from socket import *
import threading

BUFFERSIZE = 2048

serverPort = 1234

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))

#become a server socket
serverSocket.listen(3)

print "Server ready..."

#connection socket list
connectSocket_list = []


def broadcast(msg):
	try:
		for c in connectSocket_list:
			c.send(msg)
	except:
		pass


def recv_msg(connectionSocket):
	try:
		while True:
			msg = connectionSocket.recv(BUFFERSIZE)	
			if "QUIT" != msg:
				msg = "Client " + str(connectSocket_list.index(connectionSocket)) + ": " + msg
			else:
				msg = "Client " + str(connectSocket_list.index(connectionSocket)) + " has disconnected."
				connectSocket_list.remove(connectionSocket)
			print msg
			broadcast(msg)
			
			#end thread, close connection
			if msg == "QUIT":
				connectionSocket.close()
				sys.exit()
	except:
		pass

while True:
	connectionSocket, addr = serverSocket.accept()
	connectSocket_list.append(connectionSocket)
	print "Connection received from: ", addr
	
	ct = threading.Thread(target=recv_msg, args=(connectionSocket, ))
	ct.start()
	
serverSocket.close()