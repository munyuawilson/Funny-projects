import getpass as gp
list_pass=['dcn','cdjkj','zxj','wilson']
default=gp.getpass('passwd:')
if default in list_pass:
    print('Success!!')
else:
    print('Error!!')

while default not in list_pass:
    default=gp.getpass('passwd:')
    if default in list_pass:
        print('Success!!')
    else:
        print('Error!!')
        

'''
import pandas as pd
default_password='wilson'
file=pd.read_csv('passwords.csv')
for password in file.allpassords:
    #tkinter for setting the password on text box
    pass_word.set(password)
    if default_password == password:
        print('success')




'''