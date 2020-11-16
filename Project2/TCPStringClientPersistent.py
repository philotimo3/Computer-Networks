import socket

buffer_size = 500000
port = 5000

# Connect to the server
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.connect(("localhost", port))

while True:
    # Get an input string from the standard input
    # Send the string to the server
    sentence = input("Enter a message to send to server: ")
    serverSocket.sendall(sentence.encode())

    if sentence == "QUIT":
        break
    else:
        # Receive the result from the server
		# Print the result as a string
        sentence = serverSocket.recv(buffer_size).decode()
        print( sentence)


serverSocket.close()