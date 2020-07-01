#!/usr/bin/python3
""" test Place model """

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ test Place class"""
    @classmethod
    def setUp(cls):
        """steup class """
        cls.place = Place()
        cls.place.city_id = "1"
        cls.place.use_id = "2"
        cls.place.name = "toor"
        cls.place.save()

    def test_field_city_id(self):
        """ test first name field"""
        dummy_instance = Place()
        self.assertEqual(self.place.city_id, "1")
        self.assertIsInstance(self.place.city_id, str)
        self.assertEqual(dummy_instance.city_id, "")

    def test_field_user_id(self):
        """ test first name field"""
        dummy_instance = Place()
        self.assertEqual(dummy_instance.user_id, "")

    def test_field_name(self):
        """ test first name field"""
        dummy_instance = Place()
        self.assertEqual(self.place.name, "toor")
        self.assertIsInstance(self.place.name, str)
        self.assertEqual(dummy_instance.name, "")

    def test_save_method(self):
        """test save method"""
        dummy_instance = Place()
        dummy_instance.save()
        self.assertNotEqual(
            dummy_instance.created_at, dummy_instance.updated_at)

    def test_class_user(self):
        """ instance should be User; user should be subclass of BaseModel """
        self.assertTrue(issubclass(Place, BaseModel))
        self.assertIsInstance(self.place, Place)

    @classmethod
    def tearDownClass(cls):
        """clear everything"""
        del cls.place.city_id
        del cls.place.name
        del cls.place

if __name__ == '__main__':
    unittest.main()
