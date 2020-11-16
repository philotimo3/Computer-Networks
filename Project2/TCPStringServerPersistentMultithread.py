import threading
import socket
from socket import *

serverName = 'localhost'

buffer_size = 500000
serverPort = 5000

# Define a thread that will use a TCP connection socket to serve a client
#
def serve_client(client):
    while True:
        # Behavior of the thread: it will receive a string from the client
        sentence = client.recv(buffer_size).decode()
        # convert it to an uppercase string
        sentence = sentence.upper()

        #the thread should exit after it finishes serving all the requests of a client
        if sentence.isupper() == "QUIT":
            client.close()

        else:
            client.send(sentence.encode())


# Create a listening TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("The server is ready to recieve.")

while True:
    # Wait for the connection from a client
    client, addr = serverSocket.accept()
    # Create a new thread that will use the newly created TCP connection socket to serve the client
    t = threading.Thread(target=serve_client, args=(client,))
    # Start the new thread
    t.start()