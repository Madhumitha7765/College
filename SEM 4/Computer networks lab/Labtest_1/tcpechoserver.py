# Multithreaded Server

import socket
from _thread import *

server_socket=socket.socket()

host="127.0.0.1"
port=1233
ThreadCount=0
x={}
# bind host and port with the socket server which is created
try:
    server_socket.bind((host,port))
except socket.error as err:
    print(str(err))
print('Waiting for connection')
ipc=int(5)
server_socket.listen(ipc)

#for handling multiple clients
def client_thread(connection):
    connection.send(str.encode("Welcome To The Server"))
    while True:
        data = connection.recv(2048)
        option = int(data.decode("utf-8"))
        if option==1:
            c1="Server: Enter key  "
            connection.send(str.encode(c1))
            key1=int(connection.recv(1024))
            c2="Server: Enter value  "
            connection.send(str.encode(c2))
            value1 = int(connection.recv(1024))
            x={key1:value1}
            connection.send(str(x).encode("utf-8"))
        elif option==2:
            c3 = "Server: Enter key  "
            connection.send(str.encode(c3))
            key1 = int(connection.recv(1024))
            y = x.get(key1)
            connection.send(str(y).encode("utf-8"))
        elif option==3:
            connection.send(str(ipc).encode("utf-8"))

        # reply="Server received your message - "+data.decode("utf-8")
        # print("Message from client : ",end=" ")
        # print(data.decode("utf-8"))
        if not data:
            break
        # send all method sends all reply to client
        # connection.sendall(str.encode(reply))
    connection.close()

while True:
    client,address=server_socket.accept()
    print("Connected to : "+address[0]+str(address[1]))
    # available in thread module
    start_new_thread(client_thread,(client,))
    ThreadCount+=1
    print("ThreadNumber: "+str(ThreadCount))
server_socket.close()