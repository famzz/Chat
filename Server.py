import socket



host = "localhost"
port = 50007
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((host, port))
    sock.listen(1)
    conn, addr = sock.accept()
    with conn:
        print('Connected by ' + addr[0])
        message = ""
        while True:
            chunk = conn.recv(1024)
            if not chunk:
                break

            message += chunk.decode("utf-8")

            if message[:-3] == "EOD":
                break

print(message)