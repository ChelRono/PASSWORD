import string
import random

'''
 random password generator
'''

print('Welcome to password generator!')

#input length of password

length=int(input('\nEnter length of password:'))

#define data

lower=string.ascii_lowercase
upper=string.ascii_uppercase
numbers=string.digits
symbols=string.punctuation

all=lower+upper+numbers+symbols

#random

temp=random.sample(all,length)

#password

password="".join(temp)

print(password)

