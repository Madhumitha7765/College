import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

socket.connect((HOST, PORT))

print("Wait")

while(True):
    inp = input("Input> ")
    if 'mget' in inp:
        socket.send(inp.encode('utf-8'))

    elif 'mput' in inp:
        socket.send(inp.encode('utf-8'))
        out = socket.recv(1024).decode('utf-8')
        print("The Output is: ", out)
    socket.close()