#!/usr/bin/python3
""" test City model """

import unittest
from models.base_model import BaseModel
from models.city import City


class TestState(unittest.TestCase):
    """ test City model"""
    @classmethod
    def setUp(cls):
        """steup class """
        cls.city = City()
        cls.city.name = "toor"
        cls.city.state_id = "111"
        cls.city.save()

    def test_field_name(self):
        """ test first name field"""
        dummy_instance = City()
        self.assertEqual(self.city.name, "toor")
        self.assertIsInstance(self.city.name, str)
        self.assertEqual(dummy_instance.name, "")

    def test_field_state_id(self):
        """ test state_id field"""
        dummy_instance = City()
        self.assertEqual(self.city.state_id, "111")
        self.assertIsInstance(self.city.state_id, str)
        self.assertEqual(dummy_instance.state_id, "")

    def test_save_method(self):
        """test save method"""
        dummy_instance = City()
        dummy_instance.save()
        self.assertNotEqual(
            dummy_instance.created_at, dummy_instance.updated_at)

    def test_class_user(self):
        """ instance should be User; user should be subclass of BaseModel """
        self.assertTrue(issubclass(City, BaseModel))
        self.assertIsInstance(self.city, City)

    @classmethod
    def tearDownClass(cls):
        """clear everything"""
        del cls.city.name
        del cls.city

if __name__ == '__main__':
    unittest.main()
