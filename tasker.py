from tkinter import *


    


def sub():

    label=Label(root,text=task.get()).pack()
    

root=Tk()


task=StringVar()
root.title('task manager')
root.geometry("500x500")
title=Label(root,text='Tasker').pack()
entry=Entry(root,textvariable=task).pack()

button=Button(root,text='submit',command=sub).pack()

root.mainloop()