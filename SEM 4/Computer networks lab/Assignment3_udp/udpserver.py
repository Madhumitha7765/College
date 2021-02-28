import socket
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('127.0.0.1',1234))

# we use recvfrom,not recv because tcp was connection oriented in which address doesnt not change,
# but in udp address changes so we have to inout address every time in order to send back data to the address if needed
while True:
    data,addr=sock.recvfrom(1024)
    print("Client says : ", end="")
    print(data.decode('utf-8'))
    message=bytes(("Hello I am UDP Server").encode('utf-8'))

    # not send,sendto because we specifically give address
    sock.sendto(message,addr)

