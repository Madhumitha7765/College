from socket import *
import os
from time import sleep

from scapy.layers.inet import IP


def createServer():
    data = " "
    i = 0
    serversocket =  socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('192.168.0.178',8000))
        serversocket.listen(5)
        while(1):
            (clientsocket,address)=serversocket.accept()

            rd = IP()/clientsocket.recv(5000).decode()
            pieces = rd.split(" ")
            if len(pieces)>0 :
                if pieces[0]=="GET":
                    f = open(pieces[1])
                    data = "HTTP/1.1 200 OK \r\n"
                    data += "Content-Type : text/html; charset=utf-8\r\n"
                    data += "CONTENTS OF THE FILE : \n"
                    data += f.read()
                    f.close()
                if pieces[0]=="PUT":

                    if os.path.exists(pieces[1]):
                        os.remove(pieces[1])
                        print("recreating..")
                    f = open(pieces[1],"x")
                    f.close()

                if pieces[0] == "POST":

                    while os.path.exists(pieces[1]):
                        i += 1
                        name= pieces[1].split(".")
                        print(name[0])
                        print(name[1])
                        nam = name[0] + str(i) + "." + name[1]
                        f = open(nam, "x")
                        f.close()
                        break


                if pieces[0]=="DELETE":
                    file = pieces[1]
                    os.remove(file)



            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nShutting down...\n")
    except Exception as exc:
        print("\nError:\n")
        print(exc)

    serversocket.close()

print("\nServer running..")
createServer()