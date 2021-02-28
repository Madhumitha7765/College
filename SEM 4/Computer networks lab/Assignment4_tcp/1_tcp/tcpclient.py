# TCP Client program

import socket
import os
import subprocess

client_socket = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1',1234))
payload = "Hey Server"

try:
    while True:
        client_socket.send(payload.encode('utf-8'))
        data = client_socket.recv(5000)
        print("Received from server : %s " %data.decode("utf-8"))
        print('\nR - Get server routing table')
        # option s takes time of about 15 seconds as execution of netstat is done
        print('S - Get number of UDP/TCP sockets')
        print('A - Get server ARP cache')
        print('Press any character to Exit')
        option = input("Enter your option :")
        ls=['R','r','S','s','A','a']
        if str(option) not in ls : exit(0)
        client_socket.send(str(option).encode('utf-8'))
        print(client_socket.recv(5000).decode('utf-8'))
except KeyboardInterrupt:
    print("Exited by the user!")
client_socket.close()