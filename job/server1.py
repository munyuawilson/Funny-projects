import socket
import threading
import pandas as pd

port=8000
host=socket.gethostname()
list_notEmployees=[]


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))
server.listen(5)
print('[SEARCHING]........')

while True:
    conn,addr=server.accept()
    print(f'[CONNECTION ESTABLISHED].....{addr}')
    data=conn.recv(1028)
    
    df=pd.read_csv("employees.csv")
    
    if data.decode() in list(df.Email):
        print("A current employee!!")
    else:
        list_notEmployees.append(data.decode())
        dict_={'Email of Active unemployees':list_notEmployees}
        df_notEmployees=pd.DataFrame(dict_,range(len(list_notEmployees)))
        df_notEmployees.to_csv('NotEmployee.csv',index=False)
        print("Not current employee!!")
    
            
        
        
    conn.close()
