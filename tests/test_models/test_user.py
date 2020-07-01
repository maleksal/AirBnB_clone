#!/usr/bin/python3
""" test user model """

import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """ test user model"""
    @classmethod
    def setUp(cls):
        """steup class """
        cls.user = User()
        cls.user.first_name = "toor"
        cls.user.last_name = "Holberton"
        cls.user.email = "airbnb@holbertonshool.com"
        cls.user.password = "rooty1"
        cls.user.save()

    def test_field_first_name(self):
        """ test first name field"""
        dummy_instance = User()
        self.assertEqual(self.user.first_name, "toor")
        self.assertIsInstance(self.user.first_name, str)
        self.assertEqual(dummy_instance.first_name, "")

    def test_field_last_name(self):
        """ test last name field"""
        dummy_instance = User()
        self.assertEqual(self.user.password, "rooty1")
        self.assertIsInstance(self.user.password, str)
        self.assertEqual(dummy_instance.password, "")

    def test_field_email(self):
        """test email field"""
        dummy_instance = User()
        self.assertTrue(self.user.email, "airbnb@holbertonshool.com")
        self.assertIsInstance(self.user.email, str)
        self.assertEqual(dummy_instance.email, "")

    def test_field_password(self):
        """ test password field """
        dummy_instance = User()
        self.assertEqual(self.user.last_name, "Holberton")
        self.assertIsInstance(self.user.last_name, str)
        self.assertEqual(dummy_instance.last_name, "")

    def test_save_method(self):
        """test save method"""
        dummy_instance = User()
        dummy_instance.save()
        self.assertNotEqual(
            dummy_instance.created_at, dummy_instance.updated_at)

    def test_class_user(self):
        """ instance should be User; user should be subclass of BaseModel """
        self.assertTrue(issubclass(User, BaseModel))
        self.assertIsInstance(self.user, User)

    @classmethod
    def tearDownClass(cls):
        """clear everything"""
        del cls.user.first_name
        del cls.user.last_name
        del cls.user.email
        del cls.user.password
        del cls.user

if __name__ == '__main__':
    unittest.main()
