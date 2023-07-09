import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(( ' ', 55000))
sock.listen(10)
print("Чекаю на запит!")
while True:
    conn, addr = sock.accept()
    print("Підключено:", addr)
    data = conn.recv(1024)
    print("Отримано повідомлення:", data)
    if str(data) == "b'Привіт'" :
        conn.send(bytes("Привіт, Користувач!",encoding='UTF-8'))
    if str(data) == "b 'Погода на сьогодні' " :
        conn.send(bytes("Очікується сонячна погода!",encoding='UTF-8'))
    else :
        conn.send(bytes("Питання не зрозуміле, уточніть, будь-ласка, Ваш запит!",encoding='UTF-8'))
conn.close()