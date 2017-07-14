from . import context
import unittest
from app.models.bucketlistApp import BucketlistApp


class TestUserClass(unittest.TestCase):
    '''
    This test class is used to check and ensure that the
    functionality in the BucketlistApp Class works as expected.
    '''

    def test_create_user_arguments_are_passed(self):
        bucketlistapp = BucketlistApp()
        bucketlistapp.create_user('Thegaijin', '12sd4r5', '12sd4r5')
        self.assertRaises(TypeError, "Thegaijin")
        self.assertRaises(TypeError, '12sd4r5')

    def test_create_user_successfully(self):
        bucketlistapp = BucketlistApp()
        person1 = bucketlistapp.create_user('Thegaijin', '12sd4r5', '12sd4r5')
        person2 = bucketlistapp.create_user('devGenie', '12sd4', '12sd4')
        user_count = len(bucketlistapp.user_names)
        self.assertEqual(user_count, 2)

    def test_successful_login(self):
        bucketlistapp = BucketlistApp()
        bucketlistapp.login('Thegaijin', '12sd4r5')
        password_in_credentials = bucketlistapp.usercredentials[bucketlistapp.login.username]
        self.assertEqual(bucketlistapp.loginpassword, password_in_credentials)
