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
	
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print method, requestfile, httpversion
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

	response = ""

	if method == "GET":
		
		#not asking for anything
		if not requestfile:
			response = "HTTP/1.1 200 OK\r\n\r\n"
			connectionSocket.send(response)
		#asking for a file and it exists
		elif os.path.isfile(requestfile):
			response = "HTTP/1.1 200 OK\r\n\r\n"
			connectionSocket.send(response)
			with open(requestfile, "r") as f:
				for line in f:
					# print line
					connectionSocket.send(line)
		#file does not exist
		else:
			response = "HTTP/1.1 404 Not Found\r\n\r\n"
			connectionSocket.send(response)

	elif method == "POST":
		#check for header "File: "
		for m_i in range(len(msg)):

			if "File:" in msg[m_i]:
			
				print "Creating file..."

				makefile = msg[m_i][5:-1] #the -1 to remove carriage return
				open(makefile, 'a').close()
				
				print "CREATED: ", makefile
			
				response = "HTTP/1.1 200 OK\r\n\r\n"
				break
			
			else:
				response = "HTTP/1.1 500 Internal Server Error\r\n\r\n"
		
		connectionSocket.send(response)

	elif method == "OPTIONS":
		response = "HTTP/1.1 200 OK\r\n"
		response += "Allow: POST,OPTIONS,GET,HEAD\r\n\r\n"
		connectionSocket.send(response)
	
	connectionSocket.close()
	print "CLOSED: connection received from ", addr
	raise KeyboardInterrupt
	
def recv_msg(connectionSocket):
	try:
		while True:
			msg = connectionSocket.recv(BUFFERSIZE)
			# msg = "Client " + str(connectSocket_list.index(connectionSocket)) + ": " + msg
			print msg
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