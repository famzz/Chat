import sqlite3
from threading import Lock


class UserManager:
    def __init__(self):
        self.lock = Lock()
        try:
            self.lock.acquire()
            self.database = sqlite3.connect("C:\\Users\\Fahim\\Desktop\\Development\\Python\\Chat\\database\\users.db")
            self.cursor = self.database.cursor()
        finally:
            self.lock.release()

    def add_user(self, username, password):
        try:
            self.lock.acquire()
            friends = ""
            self._execute('''INSERT INTO users(username, password, friends) VALUES(?,?,?)''', (username, password,
                                                                                               friends))
        finally:
            self.lock.release()

    def add_friend(self, username, friend_name):
        try:
            self.lock.acquire()
            friends_list = self.get_friends_list(username)
            friends_list.append(friend_name)
            friends_list = ",".join(friends_list)
            self._execute('''UPDATE users SET friends = ? WHERE username = ?''', (friends_list, username))
        finally:
            self.lock.release()

    def update_password(self, username, new_password):
        try:
            self.lock.acquire()
            self._execute('''UPDATE users SET password = ? WHERE username = ?''', (username, new_password))
        finally:
            self.lock.release()

    def get_password(self, username):
        try:
            self.lock.acquire()
            self.cursor.execute('''SELECT password FROM users WHERE username=?''', (username,))
            return self.cursor.fetchone()[0]
        finally:
            self.lock.release()

    def get_friends_list(self, username):
        try:
            self.lock.acquire()
            self.cursor.execute('''SELECT friends FROM users WHERE username=?''', (username,))
            friends = self.cursor.fetchone()[0]
            friends_list = friends.split(",")
            return friends_list
        finally:
            self.lock.release()

    def _execute(self, query, parameters):
        self.cursor.execute(query, parameters)
        self.database.commit()
