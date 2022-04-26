class Credentials:
    """
    Class that generates new instances of passwords
    """

    credentials_list=[]

    def __init__(self,user_name, user_password):


        self.user_name = user_name
        self.password=user_password
 
    def save_credentials(self):

        '''
        save_password method saves password objects into password_list
        '''

        Credentials.credentials_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list