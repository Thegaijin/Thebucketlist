from app import Lists
from unittest import TestCase


class TestUserClass(TestCase):
    '''
    This test class is used to check and ensure that the functionality in the Lists Class works as expected.
    That the class has a Create_list, view_list, update_list and delete_list methods.
    That the parameter datatypes are the right ones
    '''

    def SetUp(self):
        try:
            self.new_list = Lists()
        except NameError as e:
            raise 'Check the class name and try again'

    def test_Lists_instance(self):
        self.assertIsInstance(
            self.new_list, Lists, msg='The object should be an instance of the Lists class')

    def test_if_class_has_create_list_method(self):
        getattr(Lists, 'create_list', 'None')

    def test_if_class_has_view_list_method(self):
        getattr(Lists, 'view_list', 'None')

    def test_if_class_has_update_list_method(self):
        getattr(Lists, 'update_list', 'None')

    def test_if_class_has_delete_list_method(self):
        getattr(Lists, 'delete_list', 'None')
