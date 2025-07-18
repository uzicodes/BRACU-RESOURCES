# -*- coding: utf-8 -*-
"""task-2 server.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tHY1fMBWYFtnw5FxB_2YCXIAY3FvRz8L
"""

import socket

def count_vowels(message):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in message if char in vowels)

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('0.0.0.0', 12345)
    server_socket.bind(server_address)
    server_socket.listen(5)

    print("Server is running and waiting for connections...")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received message: {data}")

        vowel_count = count_vowels(data)
        if vowel_count == 0:
            response = "Not enough vowels"
        elif vowel_count <= 2:
            response = "Enough vowels I guess"
        else:
            response = "Too many vowels"

        client_socket.send(response.encode('utf-8'))
        print(f"Response sent: {response}")

        client_socket.close()

if __name__ == "__main__":
    start_server()