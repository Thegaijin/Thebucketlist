import unittest
from app import User


class TestUserClass(TestCase):
    '''
    This test class is used to check and ensure that the functionality in the User Class works as expected.
    That the class has a login method and a registration method.
    That the parameter datatypes are the right ones
    '''

    def SetUp(self):
        try:
            self.new_user = User()
        except NameError as e:
            raise 'Check the class name and try again'

    def test_User_instance(self):
        self.assertIsInstance(
            self.new_user, User, msg='The object should be an instance of the User class')

    def test_if_class_has_login_method(self):
        getattr(User, 'login', 'None')

    def test_if_class_has_register_method(self):
        getattr(User, 'register', 'None')
