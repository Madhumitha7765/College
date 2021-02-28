import socket

sock = socket.socket()
host=socket.gethostname()
port=8080

sock.connect((host,port))
print("Connected to server")
msg = sock.recv(1024)
msg=msg.decode()
print("Server Message: ",msg)

while 1:
    msg=sock.recv(1024)
    msg=msg.decode()
    print("Server: ",msg)
    msg=sock.recv(1024)
    msg=msg.decode()
    print("Server: ",msg)
    new_msg = input(str(">>"))
    new_msg = new_msg.encode()
    sock.send(new_msg)
    print("Message Sent")