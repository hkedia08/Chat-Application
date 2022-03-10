from socket import socket, AF_INET, SOCK_DGRAM
import sys
port = int(sys.argv[2])
host = sys.argv[1]
serversocket = socket(AF_INET, SOCK_DGRAM)
serversocket.bind((host, port))
print(f'Server is binded on IP: {host} and port: {port}')
while True:
    (message, clientaddress) = serversocket.recvfrom(2048)
    print(f'{clientaddress}: {message.decode()}')
    new_data = message.decode().upper()
    serversocket.sendto(new_data.encode(), clientaddress)
