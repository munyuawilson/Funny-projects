from tkinter import *
import socket
import threading


def send():
    frame=Frame(root,bg='white',).grid(row=1 ,column =2)
    Label(frame,text=msg_send.get(),fg='orange').grid(row=1 ,column =1)
    

root=Tk()
msg_send=StringVar()
root.title('chat app')
root.geometry('500x500')
root.config(
background='green')



message_send=Entry(root,width=50,textvariable=msg_send).place(x=0,y=100)
send_button=Button(root, text='send',command=send).grid(row=10 ,column =4,pady=1)








root.mainloop()
