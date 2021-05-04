from socket import *

if __name__=="__main__":
    print("\nAccess http://localhost:9555/")
    sock =  socket(family=AF_INET,type=SOCK_STREAM)
    try:
        sock.bind(('localhost',9555))
        sock.listen(10)
        while True:
            (clientsocket,address)=sock.accept()

            data = "HTTP/1.1 200 OK \r\n"
            data += "Content-Type : text/html; charset=utf-8\r\n"
            data += "\r\n"
            data += "<html><body>Hii Razeen</body></html>"

            clientsocket.sendall(data.encode())
            clientsocket.shutdown(SHUT_WR)
    except KeyboardInterrupt:
        print("\nClosing...\n")
    except Exception as exc:
        print("\nError:\n")
        print(exc)

    sock.close()