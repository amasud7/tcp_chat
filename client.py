import socket
import threading

HOST = socket.gethostbyname(socket.gethostname())
port = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, port))
    s.send(b"Hello world")
    data = s.recv(1024)

    print(f"Server reply: {data}")

