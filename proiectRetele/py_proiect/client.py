import socket
import threading
import json

def check_user(nickname, password):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for user in users:
            if user['nickname'] == nickname and user['password'] == password:
                return True
        return False

nickname = input("Enter your nickname: ")
password = input("Enter your password: ")

if not check_user(nickname, password):
    print("Invalid credentials!")
    exit()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('37.120.249.45', 8413))

def receive():
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            elif message == 'PASS':
                client.send(password.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()