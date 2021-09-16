from .constants import *

import socket

class Server:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        self.sock.bind((host, port))
        self.sock.listen(10)
        self.run()

    def handler(sock, addr):
        pass

    def run(self):
        while True:
            # Accept new connections in an infinite loop.
            client_sock, client_addr = self.sock.accept()
            print('New connection from', client_addr)

            chunks = []
            while True:
                # Keep reading while the client is writing.
                data = client_sock.recv(2048)
                if not data:
                    # Client is done with sending.
                    break
                chunks.append(data)
                print('\n', data)


            print("message: ", chunks)
            client_sock.sendall(b''.join(chunks))
            client_sock.close()

if __name__ == "__main__":
    Server()
