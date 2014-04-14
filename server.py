#server.py

from socket import *

BUFFERSIZE = 2048

serverPort = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print "Server ready..."

connectionSocket, addr = serverSocket.accept()
msg = connectionSocket.recv(BUFFERSIZE)
print addr, ": ", msg
connectionSocket.close()

























"""

serverSocket = socket(AF_INET, SOCK_DGRAM) #instantiate socket
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #so we could reuse socket
# serverSocket.bind(('', serverPort))


print "Server ready..."

while 1:
	message, clientAddress = serverSocket.recvfrom(BUFFERSIZE)
	print clientAddress, ": ", message

"""