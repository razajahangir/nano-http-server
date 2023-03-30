import socket

class nanoSocket:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def bind(self):
        self.server_socket.bind((self.host, self.port))

    def listen(self, backlog=1):
        self.server_socket.listen(backlog)

    def accept(self):
        return self.server_socket.accept()

    def close(self):
        self.server_socket.close()

    
