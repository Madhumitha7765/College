import socket
import os
import subprocess

# socket object created
# afinet-denotes ipv4 family,sockstream-tcp transmission
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# server binds socket with ip address and port no
# since we run on localhost,ip add is 127.0.0.1
# double brackets because methods like bind,connect take only one input argument
server_socket.bind(('127.0.0.1',1234))

# server starts to listen after binding
# listen takes a backlog parameter
# 5 denotes that 5 connections are kept waiting if server is busy
# if 6th socket try to connect then server refuses the connection
server_socket.listen(10)

# make while loop,start to accept all incoming connection
while True:

    print("server waiting for connection")
    # accept method initiate a connection with the client
    # accept method return new socket object representing the connection and tuple holding address of the client
    client_socket, addr = server_socket.accept()
    print("client connected from ",addr)

    # another infinite loop to get data and send data to the client
    while True:
        # receive data from client using recv method
        # recv receives atmost 1024 bytes
        data=client_socket.recv(1024)
        # if data not received or end,then break loop
        # we  must decode data to utf8 string
        if not data or data.decode("utf-8")=='END':
            break
        print("received from client : %s " %data.decode("utf-8"))
        # we put sending data commands into try block
        try:
            # string is not sent,only bytes are sent
            # decode bytes to utf8
            client_socket.send(bytes("Hey Client", 'utf-8'))
        except: print("Exited by the user")
    # close the connection
    client_socket.close()
server_socket.close()

