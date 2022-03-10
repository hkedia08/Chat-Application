from socket import socket, AF_INET, SOCK_STREAM
import sys
port = int(sys.argv[2])
host = sys.argv[1]
serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen(5)
print(f'Server is listening on IP: {host} and port: {port}')
while True:
    (clientsocket, address) = serversocket.accept()
    print(f'Client {address} connected')
    while True:
        data = clientsocket.recv(1024)
        print(f'Client {address} message: {data.decode()}')
        if not data.decode():
            clientsocket.close()
            break
        new_data = data.decode().upper()
        clientsocket.send(new_data.encode())

