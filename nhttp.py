import socket

HOST, PORT = '127.0.0.1', 8080;
BUFFER_SIZE = 1024

# Create socket using IP version 4 (AF_INET) on TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to port and address
server_socket.bind((HOST, PORT))

# Listen to incoming TCP connections
server_socket.listen(1)
print(f"Listening on {HOST}:{PORT}")

# Define HTTP status line and headers
status_line = "HTTP/1.1 200 OK"
headers = "Content-Type: text/plain; charset=UTF-8"
body = "Hello, World!"

# Combine the parts into a single response
http_response = f"{status_line}\r\n{headers}\r\n\r\n{body}".encode("utf-8")


while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection from {client_address}")

    # Receive the http request
    request = client_socket.recv(BUFFER_SIZE)
    print(f"Received request: {request}")

    # Send the http response
    client_socket.sendall(http_response)

    # Close the connection
    client_socket.close()
