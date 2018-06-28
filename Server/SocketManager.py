from threading import Lock


class SocketManager:
    def __init__(self):
        self.sockets = {}
        self.socket_lock = Lock()

    def add_client_socket(self, username, socket):
        self.socket_lock.acquire()
        try:
            self.sockets[username] = socket
        finally:
            self.socket_lock.release()

    def get_client_socket(self, username):
        self.socket_lock.acquire()
        try:
            return self.sockets[username]
        finally:
            self.socket_lock.release()
