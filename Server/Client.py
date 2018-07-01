import threading
import select
from Util.CommunicationHelper import receive_message, send_message


class Client(threading.Thread):
    def __init__(self, sock, addr, conversation_manager, socket_manager):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.conversation_manager = conversation_manager
        self.socket_manager = socket_manager
        self.start()

    def run(self):
        while 1:
            message = None
            if select.select([self.sock], [], [], 0.1)[0]:
                message = receive_message(self.sock)
            if message:
                message = message.decode("utf-8")

                username, message = message.split(":", 1)

                if "ESTABLISHCONNECTION" in message:
                    recipient = message.split("ESTABLISHCONNECTION", 1)[1]
                    self.conversation_manager.add(username, recipient)
                    self.socket_manager.add(username, self.sock)
                else:
                    recipient = self.conversation_manager.get(username)
                    recipient_socket = self.socket_manager.get(recipient)
                    send_message(recipient_socket, message)
