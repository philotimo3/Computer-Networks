from socket import *

serverName = 'localhost'
serverPort = 5000
while True:
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    sentence = input("Input a lowercase sentence: ")
    if sentence == "Quit":
        break
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print(modifiedSentence.decode())
    clientSocket.close()

