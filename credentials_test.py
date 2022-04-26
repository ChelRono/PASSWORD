from credentials import Credentials
import unittest


class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credentials = Credentials("Val", "val123")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.user_name,"Val")
        self.assertEqual(self.new_credentials.password,"val123")
        
    def test_save_credentials(self):
        '''
        test_save_password test case to test if the password object is saved into
         the password list
        '''
        self.new_credentials.save_credentials() # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list),1)

    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
            '''
            test_save_multiple_credentials to check if we can save multiple credentials
            objects to our credential_list
            '''
            self.new_credentials.save_credentials()
            test_credentials = Credentials("Test", "bye14") # new credentials
            test_credentials.save_credentials()
            self.assertEqual(len(Credentials.credentials_list),2)
   
    def delete_credentials(self):

        '''
        delete_credential method deletes a saved credential from the credential_list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a number and returns a username that matches that name.

        Args:
            name: username to search for
        Returns :
            password of person that matches the username
        '''

        for credentials in cls.credentials_list:
            if credentials.username == user_name:
                return user_name

    @classmethod
    def credentials_exist(cls,user_name):
        '''
        Method that checks if a credential exists from the credential list.
        Args:
            credential: Credentials to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for user_name in cls.credentials_list:
            if Credentials.user_name == user_name:
                    return True

            return False

        

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''

        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)

if __name__ == '__main__':
    unittest.main()