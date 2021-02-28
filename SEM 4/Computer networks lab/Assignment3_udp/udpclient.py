import socket
import os

client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="This is a message from your client"
client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',1234))

data,addr=client_socket.recvfrom(1024)
print("Server says : ",end="")
print(data.decode('utf-8'))
client_socket.close()