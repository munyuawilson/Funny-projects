from tkinter import *
#button functions

def bc():
    ro=Tk()
    ro.title('scgfv')
    ro.mainloop()
def one():
    a.insert(0,'fgsjhy',END)    
def two():
    b=a.get()
    b.insert(0,'fgsjhy',END)
def three():
    a.set('3')
def four():
    a.set('4')
def five():
    a.set('5')
def six():
    a.set('6')
def seven():
    a.set('7')
def eight():
    a.set('8')
def nine():
    a.set('9')
def zero():
    a.set('0')

#GUI OF THE CALCULATOR
root=Tk()

a=StringVar()
root.title('calculator')
root.geometry("700x300")
root.config(
   background='aqua'
    
)

start=Label(root,text='####Willis Calc .001#####', ).grid(row=0,column=3)

frame=Frame(root,bg='white').grid()
entry=Entry(root,width=30,bg='white',fg='orange',textvariable=a).grid(row=2,column=3)



#operators
addition=Button(root,text='+',height=1,width=10).grid(row=10,column=1)
subtraction=Button(root,text='-',height=1,width=10).grid(row=10,column=2)
multiplication=Button(root,text='*',height=1,width=10).grid(row=10,column=3)
division=Button(root,text='/',height=1,width=10).grid(row=10,column=4)
#numbers
n_one=Button(root,text='1',height=1,width=11,command=one).grid(row=11,column=1)
n_two=Button(root,text='2',height=1,width=11,command=two).grid(row=11,column=2)
n_three=Button(root,text='3',height=1,width=11,command=three).grid(row=11,column=3)
n_four=Button(root,text='4',height=1,width=11,command=four).grid(row=11,column=4)
n_five=Button(root,text='5',height=1,width=11,command=five).grid(row=12,column=1)
n_six=Button(root,text='6',height=1,width=11,command=six).grid(row=12,column=2)
n_seven=Button(root,text='7',height=1,width=11,command=seven).grid(row=12,column=3)
n_eight=Button(root,text='8',height=1,width=11,command=eight).grid(row=12,column=4)
n_nine=Button(root,text='9',height=1,width=11,command=nine).grid(row=13,column=1)
n_zero=Button(root,text='0',height=1,width=11,command=zero).grid(row=13,column=2)
equals=Button(root,text='=',height=1,width=11).grid(row=13,column=3)
delete=Button(root,text='DEL',height=1,width=11,bg='red').grid(row=13,column=4)
b=Button(root,command=bc,text='rott').grid(row=15,column=1)






root.mainloop()


