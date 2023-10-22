import random
r=random.randrange(3)
g=input('guess a number from zero to three: ')
if g == r:
    print('correct!!')
else:
    print('try again!!')
