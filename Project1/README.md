# Computer-Networks

For this project I ran the given server code and edited the client code so that the client both allowed the user to continue to send multiple requests (instead of just one as it was originally written) stopped the program when the user typed in “Quit”. 

Project 1 for Computer Networks class taken in Spring of 2020

Background
In class, we used a simple application to introduce socket programming. The behaviors of the application are as follows:
1. client reads a line of characters (data) from its keyboard and sends data to server.
2. server receives the data and converts characters to uppercase.
3. server sends modified data to client; continue to run to serve other clients.
4. client receives modified data and displays line on its screen and then exits.
We assume that both the client and the server run on the same machine.

Project Requirements:

Please make changes in the client code, so that the client allows the user to continue to send multiple requests until the user types in “Quit”. This means that the client process should not exit after the user sends one request and receives one response. Instead, the client process should be able to receive subsequent inputs from the user. You need to have a loop in the client code, so that it can accept the user request until the user explicitly types in “Quit.”

Please run the given code on your machine to understand the code and the original application, before you make changes to the code. In this project, please DO NOT change anything on the server side. Only change the client codes so that they can work correctly with the servers and meet the requirements. The given TCP server code features a non-persistent implementation, which uses a separate connection for each request. Thus, for your TCP client to interact correctly with the given TCP server, your client should also use a non-persistent implementation to send multiple requests from the user. This means, your client should constantly open and close connections if the user has multiple requests to send.

You can use either Python or Java to complete the project. (I chose Python)
•	The modified UDP client code. (preferred file name: UDPClient.py or UDPClient.java)
•	The modified TCP client code. (preferred file name: TCPClient.py or TCPClient.java)

Python Socket Programming (using Python 3)
If we use UDP sockets, we have the following code:
# Python code for the UDP client:

from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("Input a lowercase sentence: ")
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()

# Python code for the UDP server:

from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive.")
while True:
   message, clientAddress = serverSocket.recvfrom(2048)
   modifiedMessage = message.decode().upper()
   print("message to be sent back: ")
   print(modifiedMessage)
serverSocket.sendto(modifiedMessage.encode(), clientAddress)
  
If we use TCP sockets, we have the following code:
# Python code for the TCP client

from socket import *

serverName = 'localhost'
serverPort = 5000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence = input("Input a lowercase sentence: ")
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print(modifiedSentence.decode())
clientSocket.close()
  
# Python code for the TCP server

  from socket import *

serverPort = 5000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print("The server is ready to receive.")
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
