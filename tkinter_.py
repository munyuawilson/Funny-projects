from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='Warning',message='hi')


root=Tk()
root.title('hahaha')
button=Button(root,text='click me!',command=click).pack(side='left')

frame=Frame(root,bg='green').pack(expand=True,fill='both')


root.mainloop()