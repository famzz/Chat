from threading import Lock


class SafeDict:
    def __init__(self):
        self.dict = {}
        self.lock = Lock()

    def add(self, key, value):
        self.lock.acquire()
        try:
            self.dict[key] = value
        finally:
            self.lock.release()

    def get(self, key):
        self.lock.acquire()
        try:
            return self.dict.get(key)
        finally:
            self.lock.release()
