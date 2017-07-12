from . import context
import unittest
from app.models.users import User


class TestUserClass(unittest.TestCase):
    '''
    This test class is used to check and ensure that the functionality in the User Class works as expected.
    That the class has a login method and a registration method.
    That the parameter datatypes are the right ones
    '''

    def setUp(self):
        try:
            self.new_user = User("Thegaijin")
        except NameError as e:
            raise 'Check the class name and try again'

    def test_User_instance(self):
        self.assertIsInstance(
            self.new_user, User, msg='The object should be an instance of the User class')

    def test_if_class_has_login_method(self):
        getattr(User, 'create_list', 'None')

    def test_if_class_has_register_method(self):
        getattr(User, 'register', 'None')

    def test_if_class_has_add_item_method(self):
        getattr(User, 'add_item', 'None')

    def test_if_class_has_view_item_method(self):
        getattr(User, 'view_item', 'None')

    def test_if_class_has_update_item_method(self):
        getattr(User, 'update_item', 'None')

    def test_if_class_has_delete_item_method(self):
        getattr(User, 'delete_item', 'None')

    def test_if_class_has_create_list_method(self):
        getattr(User, 'create_list', 'None')

    def test_if_class_has_view_list_method(self):
        getattr(User, 'view_list', 'None')

    def test_if_class_has_update_list_method(self):
        getattr(User, 'update_list', 'None')

    def test_if_class_has_delete_list_method(self):
        getattr(User, 'delete_list', 'None')
