import socket
from threading import *
import Util
from Server.ConversationManager import ConversationManager
from Server.SocketManager import SocketManager

ip = '127.0.0.1'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))

conversation_manager = ConversationManager()
socket_manager = SocketManager()


class Client(Thread):
    def __init__(self, sock, addr):
        Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.start()

    def run(self):
        while 1:
            message = Util.receive_message(self.sock)

            username, message = message.split(":", 1)

            if "ESTABLISHCONNECTION" in message:
                recipient = message.split("ESTABLISHCONNECTION", 1)[1]
                conversation_manager.add_conversation(username, recipient)
                socket_manager.add_client_socket(username, self.sock)
            else:
                recipient = conversation_manager.get_recipient(username)
                recipient_socket = socket_manager.get_client_socket(recipient)
                Util.send_message(recipient_socket, message)


s.listen(2)
while 1:
    client_socket, address = s.accept()
    Client(client_socket, address)
