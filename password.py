class Password:
    """
    Class that generates new instances of passwords
    """

    password_list=[]

    def __init__(self,user_name):


        self.user_name = user_name

    def save_password(self):

        '''
        save_password method saves password objects into password_list
        '''

        Password.password_list.append(self)