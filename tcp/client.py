from socket import socket, AF_INET, SOCK_STREAM
import sys
serverport = int(sys.argv[2])
serverhost = sys.argv[1]
clientsocket = socket(AF_INET, SOCK_STREAM)
clientsocket.connect((serverhost, serverport))

while True:
    message = input('Input your message: ')
    if not message:
        clientsocket.close()
        break
    clientsocket.sendto(message.encode(), (serverhost, serverport))
    new_message, serveraddress = clientsocket.recvfrom(2048)
    print(new_message.decode())
