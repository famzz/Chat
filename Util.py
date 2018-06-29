import struct


def send_message(sock, msg):
    msg = msg.encode("utf-8")
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)


def receive_message(sock):
    raw_length = receive_all(sock, 4)
    if not raw_length:
        return None

    length = struct.unpack('>I', raw_length)[0]

    return receive_all(sock, length)


def receive_all(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data
