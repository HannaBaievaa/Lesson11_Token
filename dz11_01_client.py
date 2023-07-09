#client

import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 55000))
sock.send(bytes("Це клієнт, чекаю відповідь", encoding='UTF-8'))
data = sock.recv(1024)
sock.close()
print(data)