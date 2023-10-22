#Mess app logic
import time
import random


print('Food Available')
name_customer=input('Customer name:')
receipt_no=random.randrange(1000,1800)
Hotel_name="##########KarU Mess########"
Date=time.time()
time=time.ctime(Date)
dict_food={
    'tea':10,
    'ndazi':10,
    'ugali':10,
    'beans':15,
    'rice':15,
    'cabbage':5,
    'Ndengu':15,
    'beef':40,

}
list_=[]
print(dict_food)


n_or_c=int(input('1.start\n'))
while n_or_c==  1:
    select=input('Order food:').lower()
    list_.append(select)
    n_or_c=int(input('1.next\n2.checkout\n'))
    
    if n_or_c==2:
        pass
pric_li=[]
#Make a receipt
for l in list_:
    
    
    if select in  dict_food:
        with open('receipt.txt','w') as file:
            file.write('\t\t\t\t\t\t'+Hotel_name+'\n\nName:\t'+name_customer + '\nReceipt No:'+ str(receipt_no) +'\t\tDate:'+str(time) +'\n'+ l.upper()+'='+str(price)+'\n\t\t\t\t\t\tTHANKYOU')
            file.close()
    else:
        print('try again')
print('Thankyou')
print(list_)

