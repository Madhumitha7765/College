import socket

from scapy.layers.inet import IP

mysock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

mysock.connect(('192.168.0.178',8000))
ch = input("\nChoice : ")
if int(ch) ==1:

    cmd = IP()/'GET filename.html HTTP/1.0\r\n'.encode("utf-8")
elif int(ch) ==2:
    cmd = 'PUT putworked.txt'.encode()
elif int(ch) ==3:
    cmd = 'DELETE putworked.txt'.encode()
elif int(ch) ==4:
    cmd = 'POST putworked.txt'.encode()

mysock.send(cmd)

while True:
    data =  mysock.recv(1024)
    if len(data)<1:
        break
    print(data.decode(),end=" ")

mysock.close()