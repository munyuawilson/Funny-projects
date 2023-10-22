import socket
import threading

port=8080
host=socket.gethostname()
server=socket.socket(socket.AF_INET,socket.SOCK_STRcEAM)
server.bind((host,port))
server.listen(5)
print('[SEARCHING]........')

while True:
    conn,addr=server.accept()
    print(f'[CONNECTION ESTABLISHED].....{addr}')
    data=conn.recv(1028)
    
            
        
        
    conn.close()
