#!/usr/bin/python3
""" test user model """

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ test State model"""
    @classmethod
    def setUp(cls):
        """steup class """
        cls.state = State()
        cls.state.name = "toor"
        cls.state.save()

    def test_field_name(self):
        """ test first name field"""
        dummy_instance = State()
        self.assertEqual(self.state.name, "toor")
        self.assertIsInstance(self.state.name, str)
        self.assertEqual(dummy_instance.name, "")

    def test_save_method(self):
        """test save method"""
        dummy_instance = State()
        dummy_instance.save()
        self.assertNotEqual(
            dummy_instance.created_at, dummy_instance.updated_at)

    def test_class_user(self):
        """ instance should be User; user should be subclass of BaseModel """
        self.assertTrue(issubclass(State, BaseModel))
        self.assertIsInstance(self.state, State)

    @classmethod
    def tearDownClass(cls):
        """clear everything"""
        del cls.state.name
        del cls.state

if __name__ == '__main__':
    unittest.main()
