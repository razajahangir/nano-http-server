from nanoSocket import nanoSocket
from requestParser import requestParser
from router import routeRequest
from responseBuilder import buildResponse

HOST, PORT = '127.0.0.1', 8080
BUFFER_SIZE = 1024

nanoSocket = nanoSocket(HOST, PORT)
nanoSocket.bind()
nanoSocket.listen()


while True:

    # Accept an incoming connection 
    clientSocket, clientAddress = nanoSocket.accept()
    print(f"Connection from {clientAddress}")

    # Receive HTTP request
    reqBytes = clientSocket.recv(BUFFER_SIZE)

    # Parse the request
    req = requestParser.parseRequest(reqBytes)
    
    # # Route request to appropriate handler
    res = routeRequest(req)

    # Build the HTTP response
    http_res = buildResponse(res)

    # # # # Send the HTTP response
    clientSocket.sendall(http_res)

    # # # # Close the connection
    clientSocket.close()
