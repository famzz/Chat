import threading
from Util.CommunicationHelper import receive_message


class Receiver(threading.Thread):
    def __init__(self, socket, recipient):
        threading.Thread.__init__(self)
        self.socket = socket
        self.recipient = recipient
        self.stop = False
        self.message_text = None
        self.start()

    def run(self):
        while not self.stop:
            msg = receive_message(self.socket)
            if msg:
                msg = msg.decode("utf-8")
                self.message_text.insert(self.recipient + ": " + msg)

    def close(self):
        self.stop = True

    def set_message_text(self, message_text):
        self.message_text = message_text
