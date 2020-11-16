from socket import *
import socket

buffer_size = 500000
serverPort = 5000
serverName = 'localhost'

# Create a listening TCP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("The server is ready to recieve.")

while True:
    # Wait for the connection from a client
    connection, addr = serverSocket.accept()
    while True:
        # Use the established TCP connection socket to recieve a string from the client
        sentence = connection.recv(buffer_size).decode()

        # if the request is "Quit" close connection & break
        if sentence == "Quit":
            connection.close()
            break

        # Convert the string to an upper case string
        # Send back the result as a string to client using the connection
        else:
            sentence = sentence.upper()
            connection.send(sentence.encode())

