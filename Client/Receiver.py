import threading
import select
from Util.CommunicationHelper import receive_message


class Receiver(threading.Thread):
    def __init__(self, socket, recipient):
        threading.Thread.__init__(self)
        self.socket = socket
        self.recipient = recipient
        self.stoprequest = threading.Event()
        self.message_text = None
        self.start()

    def run(self):
        while not self.stoprequest.is_set():
            msg = None
            if select.select([self.socket], [], [], 0.1)[0]:
                msg = receive_message(self.socket)
            if msg:
                msg = msg.decode("utf-8")
                self.message_text.insert(self.recipient + ": " + msg)

    def join(self, timeout=None):
        self.stoprequest.set()
        super(Receiver, self).join(timeout)

    def set_message_text(self, message_text):
        self.message_text = message_text
