import socket
import threading
import time

port=8000
host=socket.gethostname()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
names=["wilson","john","smith"]
print('[SEARCHING]........')

while True:
    conn,addr=server.accept()
    print(f'[CONNECTION ESTABLISHED].....{addr}')
    data=conn.recv(1028)
    while data:
        if data.decode() in names:
            response=f"{data.decode()} was found in the database!"
            time.sleep(5)
            conn.send(response.encode())
        else:
            response=f"{data.decode()} was not found in the database!"
            time.sleep(5)
            conn.send(response.encode())
            
        
            
        
        
    conn.close()
