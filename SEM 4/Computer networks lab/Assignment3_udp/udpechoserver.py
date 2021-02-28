import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',12345))

while True:
    data,addr=sock.recvfrom(1024)
    print(data.decode('utf-8'))
    message=bytes(("Hello I am UDP Server").encode('utf-8'))
    sock.sendto(message,addr)
