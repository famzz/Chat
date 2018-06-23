import socket


host = "localhost"
port = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((host, port))
    sock.send(b"HelloEOD")

