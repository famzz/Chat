import socket
import threading
from Util.CommunicationHelper import send_message, receive_message
from tkinter import simpledialog, Tk


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
        username_window = Tk()
        username_window.focus()
        username_window.withdraw()
        self.username = simpledialog.askstring("Username", "Please enter your username", parent=username_window)
        username_window.destroy()

        recipient_window = Tk()
        recipient_window.focus()
        recipient_window.withdraw()
        self.recipient = simpledialog.askstring("Recipient", "Please enter username of user you would like to talk to",
                                                parent=recipient_window)
        recipient_window.destroy()

        self.send("ESTABLISHCONNECTION" + self.recipient)

        threading.Thread(target=self.receiver).start()

    def send(self, message):
        send_message(self.sock, prep_message(self.username, message))

    def receiver(self):
        while True:
            msg = receive_message(self.sock).decode("utf-8")
            print(self.recipient + ": " + msg)

