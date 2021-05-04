from http.client import *

flag = True
server_address='127.0.0.1'
http_client=HTTPConnection(server_address,9000)
while flag:
    print("1.GET\n2.PUT\n3.POST\n4.DELETE")
    request = input("Enter choice -  ").split()
    if request[0] == 'GET' or request[0] == 'PUT' or request[0] == 'POST' or request[0] == 'DELETE':
        http_client.request(request[0], request[1])
        rsp = http_client.getresponse()
        print(rsp.status, rsp.reason)
        msgReceived = rsp.read()
        print("Received message:", msgReceived.decode())
    else:
        break
http_client.close()


