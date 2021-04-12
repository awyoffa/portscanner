import socket

ip = socket.gethostbyname(socket.gethostname())

for port in range(10000):

    try:

        serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        serv.bind((ip, port))

    except:

        print('[OPEN] Port open :', port)

    serv.close()