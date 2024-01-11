import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect
port = 12345

# Bind to the port
server_socket.bind(('', port))

# Put the socket into listening mode
server_socket.listen(1)
print("Server is listening...")

# Establish connection with client
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive message from client
    message = conn.recv(1024).decode()
    if not message:
        break
    print(f"Client: {message}")

    # Send message to client
    message = input("Server: ")
    conn.send(message.encode())

# Close the connection
conn.close()