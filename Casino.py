from tkinter import *
import random
available_coins=100

def casino_guess():
    randomizer=random.randrange(1,3)
        
    

def red():
    red=1
    randomizer=random.randrange(1,3)
    
    
    if  randomizer==1:
            Label(root,image=card_one).grid(row=5,column=0)
    else:
            Label(root,image=card_two).grid(row=5,column=0,pady=2,sticky='n')   
    if randomizer==red:
        print('win!')
    else:
        print('lost')


def black():
    black=2 
    randomizer=random.randrange(1,3)
    if  randomizer==1:
            Label(root,image=card_one).grid(row=5,column=0)
    else:
            Label(root,image=card_two).grid(row=5,column=0,pady=2,sticky='n')
    if randomizer==black:
        print('win!')
    else:
        print('lost')
    
    
    




def bet():
    rem=available_coins-50
    Label(root,text=rem,bg='orange').grid(row=0,column=4,pady=4)
    Label(text='Betting Amount:'+str(rem),bg='orange',).grid(row=2,column=4,pady=4)


root=Tk()


root.title('CARD CASINO')
card_one=PhotoImage(file='red.png')
card_two=PhotoImage(file='black.png')
a=Button(root,image=card_one,command=red).grid(row=0,column=0)
b=Button(root,image=card_two,command=black).grid(row=0,column=1)

coins=Label(root,text=available_coins,bg='orange').grid(row=0,column=4,pady=4)
betting_button=Button(root,text='50',command=bet,bg='orange').grid(row=1,column=4,pady=4)

root.mainloop()
