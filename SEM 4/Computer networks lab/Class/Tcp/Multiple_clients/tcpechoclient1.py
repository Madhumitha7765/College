# MultipleClient1
import socket

client_socket=socket.socket()

host="127.0.0.1"
port=1233

print("Client 1 Waiting For Connection!")
try:
    client_socket.connect((host,port))
except socket.error as err:
    print(str(err))

Response=client_socket.recv(1024)
print(Response.decode("utf-8"))

while True:
    Input=input("Say Something: ")
    client_socket.send(str.encode(Input))
    response=client_socket.recv(1024)
    print(response.decode("utf-8"))

client_socket.close()