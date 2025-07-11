# -*- coding: utf-8 -*-
"""task-1 server.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tHY1fMBWYFtnw5FxB_2YCXIAY3FvRz8L
"""

import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)  # Listen on all available interfaces, port 12345
    server_socket.bind(server_address)
    server_socket.listen(5)  # Allow up to 5 simultaneous connections

    print("Server is running and waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received data from client: {data}")

        client_socket.close()

if __name__ == "__main__":
    start_server()