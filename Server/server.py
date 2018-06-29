import socket
from threading import *

from Util.CommunicationHelper import send_message, receive_message
from Util.ThreadSafeDict import SafeDict

ip = '127.0.0.1'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))

conversation_manager = SafeDict()
socket_manager = SafeDict()


class Client(Thread):
    def __init__(self, sock, addr):
        Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.start()

    def run(self):
        while 1:
            message = receive_message(self.sock)
            message = message.decode("utf-8")

            username, message = message.split(":", 1)

            if "ESTABLISHCONNECTION" in message:
                recipient = message.split("ESTABLISHCONNECTION", 1)[1]
                conversation_manager.add(username, recipient)
                socket_manager.add(username, self.sock)
            else:
                recipient = conversation_manager.get(username)
                recipient_socket = socket_manager.get(recipient)
                send_message(recipient_socket, message)


s.listen(2)
while 1:
    client_socket, address = s.accept()
    Client(client_socket, address)
