import socket
import threading
from Util.CommunicationHelper import send_message, receive_message


host = "localhost"
port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))


def prep_message(user, msg):
    return user + ":" + msg


def receiver():
    while True:
        msg = receive_message(sock).decode("utf-8")
        print(msg)


username = input("Please enter your username:\n")

recipient = input("Please enter the user that you would like to talk to:\n")

send_message(sock, prep_message(username, "ESTABLISHCONNECTION" + recipient))

threading.Thread(target=receiver).start()

while True:
    message = input("Please enter message to send to " + recipient + ":\n")
    send_message(sock, prep_message(username, message))
