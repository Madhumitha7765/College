# TCP Client program

import socket
import os
import subprocess

client_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',1234))
msg = "Hey Server"

try:
    while True:
        client_socket.send(msg.encode('utf-8'))
        data = client_socket.recv(1024)
        print("Server says : ", end=" ")
        print(data.decode("utf-8"))
        more = input("Want to send more data to server:")
        if more.lower() == 'y':
            msg = input("Enter Payload:"'')
        else:
            break
except KeyboardInterrupt:
    print("Exited by the user!")
client_socket.close()
