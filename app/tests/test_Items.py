from app import Items
from unittest import TestCase


class TestUserClass(TestCase):
    '''
    This test class is used to check and ensure that the functionality in the Items Class works as expected.
    That the class has a add_item, view_item, update_item and delete_item methods.
    That the parameter datatypes are the right ones
    '''

    def SetUp(self):
        try:
            self.new_item = Items()
        except NameError as e:
            raise 'Check the class name and try again'

    def test_Lists_instance(self):
        self.assertIsInstance(
            self.new_item, Items, msg='The object should be an instance of the Lists class')

    def test_if_class_has_add_item_method(self):
        getattr(Items, 'add_item', 'None')

    def test_if_class_has_view_item_method(self):
        getattr(Items, 'view_item', 'None')

    def test_if_class_has_update_item_method(self):
        getattr(Items, 'update_item', 'None')

    def test_if_class_has_delete_item_method(self):
        getattr(Items, 'delete_item', 'None')
