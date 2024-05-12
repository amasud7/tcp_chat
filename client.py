import socket
import threading

# asking for name 
name = input("Please enter nickname: ")

# getting host name and port number
HOST = socket.gethostbyname(socket.gethostname())
port = 5050

# creating socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connecting client socket to server
client.connect((HOST, port))

def receive():
    while True:
        try:
            msg = client.recv(1024).decode('utf-8') # messages coming directly from server not other client
            if msg == "NICK":
                client.send(name.encode('utf-8'))
            else:
                print(msg)
        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        msg = f"{name}: {input('')}"
        client.send(msg.encode('utf-8'))

# multi threading for managing receiving and writing messages at the same time 
rec = threading.Thread(target=receive)
rec.start()

wrt = threading.Thread(target=write)
wrt.start()
