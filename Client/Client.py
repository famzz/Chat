import socket
import threading
from Util.CommunicationHelper import send_message, receive_message


def prep_message(user, msg):
    return user + ":" + msg


class Client:
    def __init__(self):
        host = "localhost"
        port = 5005

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        self.username = ""
        self.recipient = ""

    def start(self):
        self.username = input("Please enter your username:\n")

        self.recipient = input("Please enter the user that you would like to talk to:\n")

        send_message(self.sock, prep_message(self.username, "ESTABLISHCONNECTION" + self.recipient))

        threading.Thread(target=self.receiver).start()

    def send(self, message):
        send_message(self.sock, prep_message(self.username, message))

    def receiver(self):
        while True:
            msg = receive_message(self.sock).decode("utf-8")
            print(self.recipient + ": " + msg)
