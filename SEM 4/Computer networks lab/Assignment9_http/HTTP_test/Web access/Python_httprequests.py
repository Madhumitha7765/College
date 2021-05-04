# Program to access from web using http requests

import requests


def options():
    print("1.GET")
    print("2.PUT")
    print("3.POST")
    print("4.DELETE")
    print("5.exit")
    choice=input("Enter your choice:")
    return choice

def clientAccess():
    x=int(options())
    if(x==1):
        URL = "http://127.0.0.1:9000/check.html"
        r = requests.get(url=URL)
    elif(x==2):
        URL='http://127.0.0.1:9000/hi,check.txt'
        r=requests.put(url=URL)
    elif(x==3):
        URL='http://127.0.0.1:9000/123456,check.txt'
        r=requests.post(url=URL)
    elif(x==4):
        URL='http://127.0.0.1:9000/check.txt'
        r=requests.delete(url=URL)
    elif(x==5):
        exit()
    else:
       print("enter valid inputs")
    msg_received=r.text
    print(r.reason,r.status_code)
    print(msg_received)

if __name__=='__main__':
    while True:
        clientAccess()