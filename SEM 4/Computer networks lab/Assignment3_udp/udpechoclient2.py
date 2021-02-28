import socket
client_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

msg="This is a message from  client 2"
client_socket.sendto(msg.encode("utf-8"),('127.0.0.1',12345))
data,addr=client_socket.recvfrom(1024)
print("Server says")
print(data.decode('utf-8'))
client_socket.close()