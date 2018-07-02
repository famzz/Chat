import socket
import sys

from Util.CommunicationHelper import send_message
from Client.Receiver import Receiver
from tkinter import simpledialog, Tk, messagebox


def prep_message(user, msg):
    return user + ":" + msg


class Client:
    def __init__(self):
        host = "localhost"
        port = 5005

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.sock.connect((host, port))
        except ConnectionRefusedError:
            error_window = Tk()
            error_window.withdraw()
            error_message = "Please start the server on the host machine at " + host + ":" + str(port)
            messagebox.showerror("Server not running", error_message)
            error_window.destroy()

            sys.exit()

        self.username = ""
        self.recipient = ""

        self.message_receiver = None

    def start(self):
        username_window = Tk()
        username_window.withdraw()
        self.username = simpledialog.askstring("Username", "Please enter your username", parent=username_window)
        username_window.destroy()

        recipient_window = Tk()
        recipient_window.withdraw()
        self.recipient = simpledialog.askstring("Recipient", "Please enter username of user you would like to talk to",
                                                parent=recipient_window)
        recipient_window.destroy()

        self.send("ESTABLISHCONNECTION" + self.recipient)

        self.message_receiver = Receiver(self.sock, self.recipient)

    def send(self, message):
        send_message(self.sock, prep_message(self.username, message))

    def set_message_text(self, message_text):
        self.message_receiver.set_message_text(message_text)

    def get_pending_messages(self):
        self.send("READYFORPENDINGMESSAGES")

    def close(self):
        self.message_receiver.join()
        self.sock.close()
