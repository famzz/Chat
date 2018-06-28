from threading import Lock


class ConversationManager:
    def __init__(self):
        self.conversations = {}
        self.conversation_lock = Lock()

    def add_conversation(self, username, recipient):
        self.conversation_lock.acquire()
        try:
            self.conversations[username] = recipient
        finally:
            self.conversation_lock.release()

    def get_recipient(self, username):
        self.conversation_lock.acquire()
        try:
            return self.conversations.get(username)
        finally:
            self.conversation_lock.release()
