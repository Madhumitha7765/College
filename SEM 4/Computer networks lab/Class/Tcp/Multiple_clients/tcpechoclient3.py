# MultipleClient3
import socket

client_socket=socket.socket()

host="127.0.0.1"
port=1233

print("Client 3 Waiting For Connection!")
try:
    client_socket.connect((host,port))
except socket.error as err:
    print(str(err))

Response=client_socket.recv(1024)
print(Response.decode("utf-8"))

while True:
    print("\nEnter action your wish to perform : ")
    print("1. mput<key,value> ")
    print("2. mget<key> ")
    print("3. IPC sockets")
    Input=input("Enter your option : ")
    client_socket.send(str(Input).encode('utf-8'))
    if int(Input)==1:
        response=client_socket.recv(1024)
        print(response.decode("utf-8"))
        o1key=input(" -- ")
        client_socket.send(str.encode(o1key))
        response = client_socket.recv(1024)
        print(response.decode("utf-8"))
        o2key = input(" -- ")
        client_socket.send(str.encode(o2key))
        print("\nThe key value pair stored - ", end="")
        print(client_socket.recv(1024).decode('utf-8'))
    elif int(Input)==2:
        response = client_socket.recv(1024)
        print(response.decode("utf-8"))
        o1key = input(" -- ")
        client_socket.send(str.encode(o1key))
        print("\nThe value of given key : " ,end="")
        print(client_socket.recv(1024).decode('utf-8'))
    elif int(Input)==3:
        print("\nIPC sockets : ",end="")
        print(client_socket.recv(1024).decode('utf-8'))


client_socket.close()