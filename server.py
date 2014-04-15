#server.py

from socket import *
import threading
import traceback
import sys
import os

BUFFERSIZE = 2048
serverPort = 60007

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))

#become a server socket
serverSocket.listen(1)

print "Server ready..."

#connection socket list
connectSocket_list = []


def broadcast(msg):
	try:
		for c in connectSocket_list:
			c.send(msg)
	except:
		pass

def respond(msg, connectionSocket):
	
	msg = msg.split('\n')
	
	firstLine = msg[0].split(' ')
	
	method = firstLine[0]
	requestfile = firstLine[1][1:]
	httpversion = firstLine[2]
	
	# print method, requestfile, httpversion

	response = ""

	if method == "GET":
		print requestfile
		if os.path.isfile(requestfile):
			response = "HTTP/1.1 200 OK\r\n\r\n"
			connectionSocket.send(response)
			with open(requestfile, "r") as f:
				for line in f:
					# print line
					connectionSocket.send(line)
		else:
			response = "HTTP/1.1 404 Not Found\r\n\r\n"

	elif method == "POST":
		response = "HTTP/1.1 200 OK\r\n\r\n"
	elif method == "OPTIONS":
		response = "HTTP/1.1 200 OK\r\n\r\n"
	
	print response
	
	connectionSocket.close()
	print "CLOSED connection received from: ", addr
	raise KeyboardInterrupt
	
def recv_msg(connectionSocket):
	try:
		while True:
			msg = connectionSocket.recv(BUFFERSIZE)
			# msg = "Client " + str(connectSocket_list.index(connectionSocket)) + ": " + msg
			# print msg
			respond(msg, connectionSocket)
			# broadcast(msg)

			#end thread, close connection
			if "QUIT" in msg:
				connectionSocket.close()
				print "Client " + str(connectSocket_list.index(connectionSocket)) + " has disconnected!"
				connectSocket_list.remove(connectionSocket)
				raise KeyboardInterrupt
	
	except KeyboardInterrupt:
		sys.exit(1)
	except Exception as e:
		traceback.print_exc()
		print e


while True:
	connectionSocket, addr = serverSocket.accept()
	print "Connection received from: ", addr

	connectSocket_list.append(connectionSocket)
	
	ct = threading.Thread(target=recv_msg, args=(connectionSocket, ))
	ct.start()
	
serverSocket.close()