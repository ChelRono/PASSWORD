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