# NETCAT IMPLEMENTATION USING SOCKETS

import socket
import time

def netcat(hn,p,content):
    # creating TCP connection
    sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((hn,p))
    # sending data
    sock.sendall(content)
    time.sleep(0.5)
    # shutdown socket
    # dissallow further t tansmission
    sock.shutdown(socket.SHUT_WR)
    ress=" "
    while True:
        data=sock.recv(1024)
        # exits if no data
        if(not data):
            break
        ress=data.decode()
    # prints received data
    print(ress)
    # close socket connection
    sock.close()


if __name__=="__main__":
    # defining hostname,port
    hostname = '127.0.0.1'
    port = 9000
    # get request to receive content of test.html file
    content="GET test.html"
    # function call to netcat
    netcat(hostname,port,content.encode())