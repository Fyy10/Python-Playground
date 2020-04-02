from socket import *

serverPort = 10492
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Server is ready')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Received message:', message.decode())
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
