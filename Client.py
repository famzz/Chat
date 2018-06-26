import socket


host = "localhost"
port = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))
sock.setblocking(0)

def send_message(username, message):
    message += "EOD"
    message = username + ":" + message
    sock.send(message.encode("utf-8"))


username = input("Please enter your username:\n")

recipient = input("Please enter the user that you would like to talk to:\n")

send_message(username, "recipient" + recipient)

while True:
    try:
        message = sock.recv(1024)
        print(message.decode("utf-8"))
    except:
        pass

    chat = input("Please enter message to send to: " + recipient + ":\n")
    send_message(username, chat)
