from tkinter import *
from pandas-1.4.1 import pandas

def but():
    greet=['hi','hello','good morning','how are you','hey']
    d=details.get()
    print(d)
    if  d in greet:
        hello=Label(root,text='hello',bg='orange').grid(row=3,column=1)
def b():
    details.delete(0,END)



root=Tk()
details=StringVar()

root.title('Text app')
root.geometry('600x500')
l=Label(root,text='message app').grid(row=1,column=1)
entry=Entry(root,textvariable=details).grid(row=2,column=1)
button=Button(root,text='send',command=but).grid(row=2,column=2)
button=Button(root,text='send',command=b).grid(row=2,column=3)


















root.mainloop()


  
