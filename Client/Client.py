import socket
import threading


host = "localhost"
port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.setblocking(0)


def send_message(user, message):
    message += "EOD"
    message = user + ":" + message
    sock.send(message.encode("utf-8"))


def receive_message():
    while True:
        try:
            incoming = sock.recv(1024)
            print(incoming.decode("utf-8"))
        except socket.error:
            pass


username = input("Please enter your username:\n")

recipient = input("Please enter the user that you would like to talk to:\n")

send_message(username, "recipient" + recipient)

reciever = threading.Thread(target=receive_message)
reciever.start()

while True:
    message = input("Please enter message to send to " + recipient + ":\n")
    send_message(username, message)
