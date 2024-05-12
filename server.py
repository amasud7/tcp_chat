# socket library for tcp sockets 
# threading for multi threading capabilites and handling multiple clients. 

import socket
import threading


# getting local ip address and picking a port that is not used
HOST = socket.gethostbyname(socket.gethostname())
port = 5050

# initializing socket object (server socket)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, port))
server.listen()


clients = []
names = []

def broadcast(msg):
    for client in clients: # send messages to each client in list 
        client.send(msg) 

# when each client connects starts receiving messages from them
def handle_client(client):
    while True: # infinite loop to continue getting messages from client
        try:
            message = client.recv(1024) # receive messages from client
            broadcast(message) # update all other users with sent messages
        except: # if there is error with client 
            index = clients.index(client) # remove client from lists and close connection 
            clients.remove(index)
            names.remove(index)
            broadcast(f"{names[index]} has left the chat.")
            client.close()
            break

def main():
    # searching for connecting clients
    while True:
        client, addr = server.accept() # client connected and its address is stored in the variables

    # asking user for nickname
        client.send("NICK".encode('utf-8'))
        name = client.recv(1064) # dont understand why this is client and not server
        clients.append(client)
        names.append(name)
        
    # Broadcasting name joined
        broadcast(f"{name} has joined the chat".encode('utf-8'))
        client.send("You have connected to server".encode('utf-8')) # telling user they have connected

    # starting a new thread for every connection
        thread = threading.Thread(target=handle_client, args=client)
        thread.start()


print("Server is listening...")
main()




