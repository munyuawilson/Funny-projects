import random
default_num=[1,2,3]

print(random.shuffle(default_num))
def random_num():
    r=random.randrange(1,4)
    return r


    
def display():
    print(f'|{random_num()}\t|\t|')
    print(f'|\t|{random_num()}\t|')
    print(f'|\t|\t|{random_num()}')
display()
a=input('>')
b=input('>')
c=input('>')
d=input('>')
e=input('>')
f=input('>')
def new_display():
    print(f'|{random_num()}\t|{a}\t|{b}')
    print(f'|{c}\t|{random_num()}\t|{d}')
    print(f'|{e}\t|{f}\t|{random_num()}')
new_display()


