import socket


host = "localhost"
port = 50007

message = input("Please enter message to send:\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    message += "EOD"
    sock.send(message.encode("utf-8"))
