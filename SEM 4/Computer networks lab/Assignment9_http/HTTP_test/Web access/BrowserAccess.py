# Program to access data from web browser using sockets
# The output of the program is a link that redirects to URL in which server is deployed

from socket import *

def createServer():
    serversocket = socket(AF_INET,SOCK_STREAM)
    try:
        serversocket.bind(('localhost',8000))
        serversocket.listen(5)
        while(1):
            (clientsocket,address)=serversocket.accept()

            data = "HTTP/1.1 200 OK \r\n"
            data += "Content-Type : text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>hey this is from web access</body></html>"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)

    except KeyboardInterrupt:
        print("\nShutting down...\n");
    except Exception as exc:
        print("\nError:\n")
        print(exc)

    serversocket.close()

if __name__=="__main__":
    print("\nAccess http://localhost:8000")
    createServer()