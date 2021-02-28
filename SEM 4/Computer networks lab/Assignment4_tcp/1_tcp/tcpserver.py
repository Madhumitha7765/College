import socket
import os
import subprocess
import sys

# socket object created
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# server binds socket with ip address and port no
server_socket.bind(('127.0.0.1',1234))

# server starts to listen after binding
server_socket.listen(10)


while True:

    print("server waiting for connection")
    client_socket, addr = server_socket.accept()
    print("client connected from ",addr)

    while True:
        data=client_socket.recv(5000)
        if not data or data.decode("utf-8")=='END':
            break
        print("Received from client : %s " %data.decode("utf-8"))
        try:
            client_socket.send(bytes("Hey Client", 'utf-8'))
            option = client_socket.recv(5000).decode("utf-8")
            if str(option) == 'R' or str(option) == 'r':
                result = subprocess.check_output(['netstat', '-r'], shell=True)
            elif str(option) == 'S' or str(option) == 's':
                result = subprocess.check_output(['netstat'], shell=True)
            elif str(option) == 'A' or str(option) == 'a':
                result = subprocess.check_output(['arp','-a'], shell=True)

            client_socket.send(result)
        except: print("Exited by the user")
    # close the connection
    client_socket.close()
server_socket.close()

