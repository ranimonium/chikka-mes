# client.py

from socket import *

# serverName = "127.0.0.1"
serverName = "10.11.3.26"
serverPort = 1234

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

msg = raw_input('Enter message: ')

clientSocket.send(msg)

clientSocket.close()



























"""

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = raw_input("Input string: ")

clientSocket.sendto(message,(serverName, serverPort))

clientSocket.close()

"""