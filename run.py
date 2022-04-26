#!/usr/bin/env python3.8
from credentials import Credentials
from User import User

def create_credentials(user_name, user_password):
    '''
    Function to create a new credentia;
    '''
    new_credentials = Credentials(user_name, user_password)
    return new_credentials

def save_credentials(password):
    '''
    Function to save credentials
    '''
    password.save_credentials()

def del_credentials(password):
    '''
    Function to delete a credentials
    '''
    password.delete_credentials()

def find_credentials(password):
    '''
    Function that finds a password by username and returns the password
    '''
    return Credentials.find_by_credentials(password)

def check_existing_credentials(user_name):
    '''
    Function that check if a password exists with that number and return a Boolean
    '''
    return Credentials.credentials_exist(user_name)

def display_credentials():
    '''
    Function that returns all the saved passwords
    '''
    return Credentials.display_credentials()

def create_user(password):
    '''
    Function to create a new credentia;
    '''
    new_user = User(password)
    return new_user

def main():
    print("Hello Welcome to your credentials list. What is your name?")
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

                            save_credentials(create_credentials(user_password, user_name)) # create and save new password.
                            print ('\n')
                            print(f"New credentials {user_name} created")
                            print ('\n')

                    elif short_code == 'dp':

                            if display_credentials():
                                    print("Here is a list of all your passwords")
                                    print('\n')

                                    for password in display_credentials():
                                            print(f"{password.user_name} {password.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any passwords saved yet")
                                    print('\n')

                    elif short_code == 'fc':

                            print("Enter the username you want to search for")

                            search_credentials = input()
                            if check_existing_credentials(search_password):
                                    search_password = find_credentials(search_password)
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

if __name__ == '__main__':

 main()