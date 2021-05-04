from http.client import *

def http_RequestHandler():
    # request command to server
    # request[0] -- command(determines subclass)
    # req[1]- data and filename
    http_client.request(request[0], request[1])
    # get response from server
    rsp = http_client.getresponse()
    # print server response and data
    print(rsp.status, rsp.reason)
    msgReceived = rsp.read()
    print("  ", msgReceived.decode())

def display_options():

    print("\n1.GET filename.extension")
    print("2.HEAD filename.extension")
    print("3.PUT data,filename.extension")
    print("4.POST data,filename.extension")
    print("5.DELETE filename.extension")
    request = input("Enter request in given format :: ")
    return request


if __name__ == "__main__":

    server_address='127.0.0.1'
    try:
        http_client=HTTPConnection(server_address,9000)
        print("CONNECTION Successful,http client connected to server")
    except:
        print("Unable to connect to http server")

    while True:

        request = display_options()
        print(request)
        request =request.split()
        x = request[0]
        # type exit to end it
        if x == 'exit':break
        elif x == 'HEAD' or x == 'PUT' or x == 'POST' or x == 'DELETE':
            http_RequestHandler()
        elif x == 'GET':
            if_modified_since_s1 = "Thu 22 Apr 2021 09:15:00 GMT"
            if_modified_since_s2 = "Thu 22 Apr 2021 11:28:00 GMT"
            req = request[1]+","+if_modified_since_s2
            http_client.request(request[0], req)
            # get response from server
            rsp = http_client.getresponse()
            # print server response and data
            print(rsp.status, rsp.reason)
            msgReceived = rsp.read()
            print("  ", msgReceived.decode())


        else:
            print("\nInvalid format please enter again\n")
            continue

    # closing client connection
    http_client.close()


