import socket

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    fin = list()

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024).decode('utf-8')
            if not data:
                break
            if 'mget' in  data:
                temp = data.split('mget')
                res = temp[1]
                res = res[1:]
                res = res[:-1]
                fin.append(res)
            elif 'mput' in  data:
                temp = data.split('mput')
                res = temp[1]
                res = res[1:]
                res = res[:-1]

                for i in range(len(fin)):
                    if fin[i][0] == res:
                        socket.send(fin[i][1].encode('utf-8'))