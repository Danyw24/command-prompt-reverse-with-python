import socket, threading

host = '192.168.0.5'
port = 55555

hacker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hacker.connect((host,port))

def recive_messages():
    while True:
        try:    
            message = hacker.recv(1024).decode('utf-8')
            if message == '@role':
                hacker.send('hack'.encode('utf-8'))
            else:
                print(message)
        except:
            print('La sesion se ha desconectado')
            hacker.close()
            


def send_messages():
    while True:
        message = input()
        hacker.send(message.encode('utf-8'))
        
        
thread1 = threading.Thread(target=recive_messages)
thread1.start()

thread2 = threading.Thread(target=send_messages)
thread2.start()
        
        