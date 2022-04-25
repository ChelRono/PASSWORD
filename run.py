#!/usr/bin/env python3.8
from password import Password

def create_password(user_name, user_password):
    '''
    Function to create a new contact
    '''
    new_password = Password(user_name, user_password)
    return new_password

def save_passwords(password):
    '''
    Function to save contact
    '''
    password.save_password()


def del_password(password):
    '''
    Function to delete a contact
    '''
    password.delete_password()    

def find_password(password):
    '''
    Function that finds a password by username and returns the password
    '''
    return Password.find_by_password(password)

def check_existing_passwords(user_name):
    '''
    Function that check if a password exists with that number and return a Boolean
    '''
    return Password.password_exist(user_name)  

def display_passwords():
    '''
    Function that returns all the saved passwords
    '''
    return Password.display_passwords()


def main():
    print("Hello Welcome to your contact list. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
                    print("Use these short codes : cp - create a new password, dp - display passwords, fp -find a password, ex -exit the password list ")

                    short_code = input().lower()

                    if short_code == 'cp':
                            print("New Password")
                            print("-"*10)

                            print ("user_name.....")
                            user_name = input()

                            print ("user_password.....")
                            user_password = input()

                             save_passwords(create_password(user_password, user_name)) # create and save new password.
                            print ('\n')
                            print(f"New password {user_name} created")
                            print ('\n')

                    elif short_code == 'dp':

                            if display_passwords():
                                    print("Here is a list of all your passwords")
                                    print('\n')

                                    for password in display_passwords():
                                            print(f"{password.user_name} {password.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any passwords saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_password = input()
                            if check_existing_passwords(search_password):
                                    search_password = find_password(search_password)
                                    print(f"{search_password.user_name}")
                                    print('-' * 20)

                                    print(f"user_name.......{search_password.user_name}")
                        
                            else:
                                    print("That password does not exist")

                    elif short_code == "ex":
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
