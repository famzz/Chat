import struct


def send_message(sock, msg):
    msg = struct.pack('>I', len(msg)) + msg.encode("utf-8")
    sock.sendall(msg)


def receive_message(sock):
    raw_length = receive_all(sock, 4)
    if not raw_length:
        return None

    length = struct.unpack('>I', raw_length)[0]

    # For some reason, unicode does not play nicely with the '£' symbol? Thinking of adding a hardcoded exception if
    # this is the only character that causes issues.
    return receive_all(sock, length).decode('utf-8', 'replace')


def receive_all(sock, n):
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data
