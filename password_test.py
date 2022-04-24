from password import Password
import unittest
import random
import string

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


class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_password = Password("Val")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_password.user_name,"Val")
        
    def test_save_password(self):
        '''
        test_save_password test case to test if the password object is saved into
         the password list
        '''
        self.new_password.save_password() # saving the new password
        self.assertEqual(len(Password.password_list),1)

   



if __name__ == '__main__':
    unittest.main()