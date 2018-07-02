import threading
from Util.CommunicationHelper import receive_message, send_message


class Client(threading.Thread):
    def __init__(self, sock, addr, conversation_manager, socket_manager, message_manager):
        threading.Thread.__init__(self)
        self.sock = sock
        self.addr = addr
        self.conversation_manager = conversation_manager
        self.socket_manager = socket_manager
        self.message_manager = message_manager
        self.start()

    def run(self):
        while 1:
            message = receive_message(self.sock)
            if message:
                message = message.decode("utf-8")

                username, message = message.split(":", 1)

                if "ESTABLISHCONNECTION" in message:
                    recipient = message.split("ESTABLISHCONNECTION", 1)[1]
                    self.conversation_manager.add(username, recipient)
                    self.socket_manager.add(username, self.sock)
                elif "READYFORPENDINGMESSAGES" in message:
                    messages = self.message_manager.get(username)
                    if messages:
                        for message in messages:
                            send_message(self.sock, message)
                else:
                    recipient = self.conversation_manager.get(username)
                    recipient_socket = self.socket_manager.get(recipient)
                    if recipient_socket:
                        send_message(recipient_socket, message)
                    else:
                        # Recipient is not online yet.
                        messages = self.message_manager.get(recipient)
                        if not messages:
                            messages = []
                        messages.append(message)
                        self.message_manager.add(recipient, messages)
                        send_message(self.sock, "NOTONLINE")
