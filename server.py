import socket
host = socket.gethostbyname(socket.gethostname())
port = 9090
clients = []
quite = False
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("start")
while not quite:
    try:
        date, adr = s.recvfrom(2048)
        print(adr)
        if adr not in clients:
            clients.append(adr)
            s.sendto(date, adr)
        print(date.decode("utf-8"))
        for client in clients:
            if adr != client:
                s.sendto(date, client)
    except:
        print("error")
s.close()

