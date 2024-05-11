# socket library for tcp sockets 
# threading for multi threading capabilites and handling multiple clients. 

import socket
import threading


# getting local ip address and picking a port that is not used
HOST = socket.gethostbyname(socket.gethostname())
port = 5050

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # with block so server closes by itself at the end
    # binding server to host and port
    # listening for potential client connections
    s.bind((HOST, port))
    s.listen()

    conn, addr = s.accept() # .accept() returns connection and address of client for connection
                                    # also blocks rest of the code until connection is found
    with conn: # conn is a socket object 
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)




