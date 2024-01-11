import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 12345

# Connect to the server on local computer
client_socket.connect(('127.0.0.1', port))

while True:
    # Send message to server
    message = input("Client: ")
    client_socket.send(message.encode())

    # Receive message from server
    message = client_socket.recv(1024).decode()
    print(f"Server: {message}")

# Close the connection
client_socket.close()