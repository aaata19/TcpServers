import socket
import threading

def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message, client)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            nicknames.remove(nickname)
            broadcast(f'{nickname} left the chat!'.encode('ascii'), _client=None)
            break

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")
        
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        client.send('PASS'.encode('ascii'))
        password = client.recv(1024).decode('ascii')
        
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat!'.encode('ascii'), _client=None)
        client.send('Connected to the server!'.encode('ascii'))
        
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

clients = []
nicknames = []

host = '37.120.249.45'
port = 8413

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

print(f"Server Started at port {port} made by gr3_13 Alina Atanasiu")
receive()