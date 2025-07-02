import socket
import threading
serverSocket = socket.socket()
serverSocket.bind(('192.168.31.113', 9123))
serverSocket.listen(1)
print('Сервер запущен')
sockets = [] # Всех кто подключился храним тут
def chatting(clientSocket_):
    while True:
        data = clientSocket_.recv(1024)
        print("Сообщение от клиента: "+data.decode())
        for client in sockets:
            client.send(data)

while True:
    print('Waiting for connection...')
    connectionSocket, addr = serverSocket.accept()
    print("Клиент подключился "+str(addr))
    sockets.append(connectionSocket)
    thread = threading.Thread(target=chatting, args=(connectionSocket, ))
    thread.start()