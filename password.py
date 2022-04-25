class Password:
    """
    Class that generates new instances of passwords
    """

    password_list=[]

    def __init__(self,user_name, user_password):


        self.user_name = user_name
        self.password=user_password
 
    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)

    @classmethod
    def display_passwords(cls):
        '''
        method that returns the password list
        '''
        return cls.password_list