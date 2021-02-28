# return ip address of domain

import socket
import sys

try:
    sock=socket.socket(socket.AF_INET , socket.SOCK_STREAM)
except socket.error as err:
    print("failed to create socket")
    print("Reason"+str(err))
    sys.exit()
print("socket created")

target_host = input("enter target host name to connect : ")
target_port = input("enter target port number : ")
try:
    sock.connect((target_host,int(target_port)))
    print("socket connected to %s on port %s" %(target_host,target_port))
    sock.shutdown(2)
except socket.error as err:
    print("failed to connect to %s on port no %s " %(target_host,target_port))
    print("Reason" + str(err))
    sys.exit()