import socket
from threading import *

ip = '127.0.0.1'
port = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))

conversations = {}
conversation_lock = Lock()


def add_conversation(username, recipient):
    conversation_lock.acquire()
    try:
        conversations[username] = recipient
    finally:
        conversation_lock.release()


def get_recipient(username):
    conversation_lock.acquire()
    try:
        return conversations.get(username)
    finally:
        conversation_lock.release()


client_sockets = {}
client_socket_lock = Lock()


def add_client_socket(username, socket):
    client_socket_lock.acquire()
    try:
        client_sockets[username] = socket
    finally:
        client_socket_lock.release()


def get_client_socket(username):
    client_socket_lock.acquire()
    try:
        return client_sockets[username]
    finally:
        client_socket_lock.release()


class Client(Thread):
    def __init__(self, sock, addr):
        Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.message = ""
        self.start()

    def run(self):
        while 1:
            chunk = self.sock.recv(1024).decode("utf-8")
            self.message += chunk

            if self.message[-3:] == "EOD":
                self.message = self.message[:-3]

                username, message = self.message.split(":", 1)
                if "recipient" in message:
                    recipient = message.split("recipient", 1)[1]
                    add_conversation(username, recipient)
                    add_client_socket(username, self.sock)
                else:
                    recipient = get_recipient(username)
                    recipient_socket = get_client_socket(recipient)
                    recipient_socket.send(self.message.encode("utf-8"))

                self.message = ""


s.listen(2)


while 1:
    clientsocket, address = s.accept()

    Client(clientsocket, address)
