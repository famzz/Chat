import socket
import threading
import Util


host = "localhost"
port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


def send_message(user, message):
    message = user + ":" + message
    Util.send_message(sock, message)


def receive_message():
    while True:
        msg = Util.receive_message(sock).decode("utf-8")
        print(msg)


username = input("Please enter your username:\n")

recipient = input("Please enter the user that you would like to talk to:\n")

send_message(username, "ESTABLISHCONNECTION" + recipient)

receiver = threading.Thread(target=receive_message)
receiver.start()

while True:
    message = input("Please enter message to send to " + recipient + ":\n")
    send_message(username, message)
