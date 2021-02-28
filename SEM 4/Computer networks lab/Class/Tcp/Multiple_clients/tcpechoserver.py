# Multithreaded Server

import socket
from _thread import *

server_socket=socket.socket()

host="127.0.0.1"
port=1233
ThreadCount=0

# bind host and port with the socket server which is created
try:
    server_socket.bind((host,port))
except socket.error as err:
    print(str(err))
print('Waiting for connection')
server_socket.listen(5)

#for handling multiple clients
def client_thread(connection):
    connection.send(str.encode("Welcome To The Server"))
    while True:
        data=connection.recv(2048)
        reply="Server received your message - "+data.decode("utf-8")
        if not data:
            break
        # send all method sends all reply to client
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    client,address=server_socket.accept()
    print("Connected to : "+address[0]+str(address[1]))
    # available in thread module
    start_new_thread(client_thread,(client,))
    ThreadCount+=1
    print("ThreadNumber: "+str(ThreadCount))
server_socket.close()