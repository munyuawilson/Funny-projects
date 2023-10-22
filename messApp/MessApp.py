from tkinter import *

def clear():
        Label(root,text='0').grid(row=15,column=3)
def submit():
    add=a.get() +b.get() +c.get()+d.get()+e.get()
    result=Label(root,text=add).grid(row=15,column=3)
    Button(root,text='clear',command=clear).grid(row=15,column=4)
def subtract():
    change=total.get()-food_pric.get()
    Label(root,text=change).grid(row=15,column=3)
    
    
    

        



root=Tk()
greenbeans=PhotoImage('beans.png')
redbeans=PhotoImage(file='red-beans.png')
ugali=PhotoImage(file='ugali.png')
mandazi=PhotoImage('mandazi.png')
tea=PhotoImage('tea.png')
cabbage=PhotoImage('cabbage.png')

icon=PhotoImage(file='Karu.png')
root.config(background='#129662')
root.iconphoto(True,icon)


root.geometry("500x500")

root.title('MessApp')
a=IntVar()
b=IntVar()
c=IntVar()
d=IntVar()
e=IntVar()
total=IntVar()
food_pric=IntVar()

label=Label(root,text='MessApp').grid(row=0,column=3,pady=2)



check=Checkbutton(root,
variable=a,
    onvalue=15,
    offvalue=0,
    text='Beans',
    
    ).grid(row=1,column=1,sticky=W)

check=Checkbutton(root,
variable=b,
    onvalue=10,
    offvalue=0,
    text='Ugali',
    
    ).grid(row=1,column=2,sticky=W)
check=Checkbutton(root,
variable=c,
    onvalue=5,
    offvalue=0,
    text='Tea',
    
    ).grid(row=1,column=4,sticky=W ,pady=4)
check=Checkbutton(root,
variable=d,
    onvalue=15,
    offvalue=0,
    text='Rice',
    
    ).grid(row=2,column=1,pady=4,sticky=W)
check=Checkbutton(root,
variable=e,
    onvalue=5,
    offvalue=0,
    text='Cabbage',
    
    ).grid(row=2,column=2,sticky=W)
button=Button(root,text='submit',command=submit).grid(row=10,column=1,pady=5)
change_calculator=Label(root,text='Change calculator').grid(row=12,column=1,pady=2)
entry=Entry(root, textvariable=total).grid(row=13,column=1,pady=2)
entry_2=Entry(root, textvariable=food_pric).grid(row=14,column=1,pady=2)
submit_=Button(root,command=subtract,text='subtract').grid(row=15,column=1,pady=2)
root.mainloop()


