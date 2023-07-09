import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(( "localhost", 55000))
sock.listen(10)
print("Чекаю на запит!")
while True:
    conn, addr = sock.accept()
    print("Підключено:", addr)
    data = conn.recv(1024)
    print("Отримано повідомлення:", data)
    words = len(data.decode('UTF-8').split(" "))
    conn.send(bytes(f"Кількість слів: {words}", encoding='UTF-8'))
    conn.close()