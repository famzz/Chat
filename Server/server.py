import socket

from Server.Client import Client
from Util.ThreadSafeDict import SafeDict

ip = '127.0.0.1'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))

conversation_manager = SafeDict()
socket_manager = SafeDict()

s.listen(2)
while 1:
    client_socket, address = s.accept()
    Client(client_socket, address, conversation_manager, socket_manager)
