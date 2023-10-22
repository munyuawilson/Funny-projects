from tkinter import *
from tkinter import messagebox

list_names=[]
list_pass=[]
details={}
def login():
    details['username']=list_names
    details['password']=list_pass
    if  (username.get() in (details['username'])) and (password.get()in (details['password'])):
        print('success!')
        
    else:
        messagebox.showwarning(title='Error!',message='Kindly input required password')
        
def new():
    if (len(username.get())==0) and (len(password.get())==0):
        Label(root,text='Input details').grid(row=4,column=1)
    else:
        list_names.append(username.get())
        list_pass.append(password.get())
    
        Label(root,text='success!').grid(row=4,column=1)
    


root=Tk()
password=StringVar()
username=StringVar()
#icon=PhotoImage(file='Karu.png')
#root.iconphoto(True,icon)
root.title('Login')
Label(root,text='Username').grid(row=1,column=1)
user_name=Entry(root,textvariable=username).grid(row=1,column=2,pady=2,sticky=W)
Label(root,text='Password').grid(row=2,column=1,pady=2,sticky=W)
pass_word=Entry(root,show='*',textvariable=password).grid(row=2,column=2,pady=2,sticky=W)
Button(root,text="LOGIN",bg='green',command=login).grid(row=3,column=1,pady=2,sticky=W)
Button(root,text='Create new account',bg='green',command=new).grid(row=3,column=3,pady=2,sticky=W)






root.mainloop()
