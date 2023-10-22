import socket

port=8000

host=socket.gethostname()

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect((host,port))

print('[CONNECTED]')



msg=input('Email adress: ')

server.send(msg.encode())

        
    
