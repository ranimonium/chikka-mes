# client.py

from socket import *
import threading

BUFFERSIZE = 2048

# serverName = "127.0.0.1"
serverName = "10.11.3.26"
serverPort = 1234

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))


def recv_msg():
	while True:
		msg = clientSocket.recv(BUFFERSIZE)
		print msg

st = threading.Thread(target=recv_msg)
st.start()

while True:
	msg = raw_input()
	clientSocket.send(msg)
	if msg == "QUIT":
		break

clientSocket.close()



























"""

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input("Input string: ")

clientSocket.sendto(message,(serverName, serverPort))

clientSocket.close()

"""