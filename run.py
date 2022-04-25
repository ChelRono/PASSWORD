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