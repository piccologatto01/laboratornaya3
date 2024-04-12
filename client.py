import socket
import os

from taskk import SOURCE_DIR

folder1 = r"C:\Users\ASUS\Documents\testfolder1"
folder2 = r"C:\Users\ASUS\Documents\testfolder2"  # Папка для синхронизации

HOST = '127.0.0.1'  # IP-адрес сервера
PORT = 5000  # Порт сервера


def handle_client(conn):
    '''
    Данная функция учтанавливает сетевое взаимодействия
    :param conn:
    :return: Создает список изменений changes
    Отправляет список изменений на сервер
    '''
    source_files = os.listdir(folder2)

    conn.sendall(str.encode(str(source_files)))

    changes = conn.recv(1024)
    changes = changes.decode('utf-8')

    for change in changes.split(','):
        if change.startswith('add'):
            file = change[4:]
            os.link(os.path.join(folder2, file), os.path.join(folder2, file))
        elif change.startswith('del'):
            file = change[4:]
            os.unlink(os.path.join(folder2, file))


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.bind((HOST, PORT))

    server.listen()

    while True:
        conn, addr = server.accept()
        handle_client(conn)


if __name__ == '__main__':
    start_server()
