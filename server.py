import socket, threading

#definimos host y puerto
host = '192.168.0.5'
port = 55555
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.bind((host, port))
server.listen()
print(f'Servidor escuchando en {host}:{port}')


clients = []
usernames = []


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            client.send(message.encode('utf-8'))
            
            
def recive_messages(client):
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            broadcast(message,client)
        except: 
            index = clients.index(client)
            username = usernames[index]     
            print(f'{username} se ha desconectado')
            broadcast(f'{username} se ha desconectado'.encode('utf-8'), client)
            clients.remove(index)
            usernames.remove(username)     
            client.close() 
            break
        
        
def recive_connections():
    while True:
        client, address = server.accept()
        m_role = '@role'.encode('utf-8')
        client.send(m_role)
        username = client.recv(1024).decode('utf-8')
        
        if username == 'hack':
            print('The hacker was connected.')
            client.send('Joined to the server!'.encode('utf-8'))
            
        elif username == 'victim':
            print('The victim was connected.')
        

        clients.append(client)
        usernames.append(username)
        
        thread = threading.Thread(target=recive_messages, args=(client,))
        thread.start()
        
        

recive_connections()
        
        
        
        
        



