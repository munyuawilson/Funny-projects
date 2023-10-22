import socket
import time
import requests


port=8000

host=socket.gethostname()

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.connect((host,port))

print('[CONNECTED]')


print("Look for a name in the database")
msg=input('Check Name>>>')

server.send(msg.encode())
start=time.time()
data=server.recv(1028)
end=time.time()
response_time=end-start
print(data.decode())

print("Response time in seconds(1 request):",response_time)
print(f"Requests\t Time\t Mode of response \n100\t {100*response_time}\t Direct mode\n200\t {200*response_time}\t Direct mode\n300\t {300*response_time}\t Direct mode\n400\t {500*response_time}\t Direct mode")



        
    
