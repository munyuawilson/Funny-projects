words=['cub*','tabl*','mone*']
g='hang'
for i in range(3):
    print(f'*\t\t\t*\t\t\t*')
for w in words:
    print(w)
first_letter=input('first letter guess: ')
if first_letter == 'e':
    print('|-------|')
    print("|       0") 
    print('|       ')
    print('|')
    print('|')
    second_letter=input('next guess: ')
    if second_letter == 'e':    
        print('|-------|')
        print("|       0") 
        print('|      /|\\')
        print('|')
        print('|')  
    
    
    third_letter=input('next guess: ')
    if third_letter == 'y':    
        print('|-------|')
        print("|       0") 
        print('|      /|\\')
        print('|      / \\')
        print('|')
else:
    print('**********daead***********')
        
