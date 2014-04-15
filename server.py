#server.py

from socket import *
import threading
import traceback


BUFFERSIZE = 2048
serverPort = 1234

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
	method = msg[0].split(' ')[0]
	httpversion = msg[0].split(' ')[2]
	
	response = ""

	if method == "GET":
		response = "HTTP/1.1 200 OK\r\n"
		response += "Connection: close\r\n\r\n"
		print response
	elif method == "POST":
		pass
	elif method == "PUT":
		pass
	connectionSocket.send(response)
	
def recv_msg(connectionSocket):
	try:
		while True:
			msg = connectionSocket.recv(BUFFERSIZE)
			print "MSG: " + msg
			respond(msg, connectionSocket)
			
			#end thread, close connection
			if msg == "QUIT":
				connectionSocket.close()
				sys.exit()
	except Exception as e:
		traceback.print_exc()
		print e


while True:
	connectionSocket, addr = serverSocket.accept()
	connectSocket_list.append(connectionSocket)
	print "Connection received from: ", addr
	
	ct = threading.Thread(target=recv_msg, args=(connectionSocket, ))
	ct.start()
	
serverSocket.close()