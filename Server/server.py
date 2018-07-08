import socket
import select
import threading

from Server.Client import Client
from Util.ThreadSafeDict import SafeDict


class Server(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.s = None
        self.clients = None
        self.stop_request = threading.Event()
        self.start()

    def run(self):
        ip = '127.0.0.1'
        port = 5005

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.bind((ip, port))

        conversation_manager = SafeDict()
        socket_manager = SafeDict()
        message_manager = SafeDict()

        self.s.listen(2)
        self.clients = []
        while not self.stop_request.is_set():
            client_socket = None
            address = None
            if select.select([self.s], [], [], 0.1)[0]:
                client_socket, address = self.s.accept()
            if client_socket:
                client = Client(client_socket, address, conversation_manager, socket_manager, message_manager)
                self.clients.append(client)

    def kill_clients(self):
        for c in self.clients:
            c.join()
            print("Killed")

    def close(self, timeout=None):
        self.kill_clients()
        self.stop_request.set()
        super(Server, self).join(timeout)

