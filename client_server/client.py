import socket
from .constants import *
class Client:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.run()

    def run(self):
        self.sock.sendall(b'Hello, world')
        self.sock.sendall(b'he said keep going')
        while True:
            to_send = input("give me a message to send: ")
            self.sock.sendall(to_send.encode())
        
        self.sock.close()
        
        
        

# # Create client socket.
# client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to server (replace 127.0.0.1 with the real server IP).
# client_sock.connect((HOST, PORT))

# # Send some data to server.
# client_sock.sendall(b'Hello, world')
# client_sock.shutdown(socket.SHUT_WR)

# # Receive some data back.
# chunks = []
# while True:
#     data = client_sock.recv(2048)
#     if not data:
#         break
#     chunks.append(data)
# print('Received', repr(b''.join(chunks)))

# # Disconnect from server.
# client_sock.close()