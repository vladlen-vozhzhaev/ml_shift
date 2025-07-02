import socket
import threading
clientSocket = socket.socket()
clientSocket.connect(('192.168.31.113', 9123))
def sendMessage():
    while True:
        message = input('Enter a message: ')
        clientSocket.send(message.encode())
def getResponse():
    while True:
        response = clientSocket.recv(1024)
        print(response.decode())


thread = threading.Thread(target=sendMessage)
thread.start()
getResponse()