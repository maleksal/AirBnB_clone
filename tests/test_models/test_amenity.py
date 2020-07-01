#!/usr/bin/python3
""" test Amenity model """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test Amenity class"""
    @classmethod
    def setUp(cls):
        """steup class """
        cls.amenity = Amenity()
        cls.amenity.name = "toor"
        cls.amenity.save()

    def test_field_name(self):
        """ test first name field"""
        dummy_instance = Amenity()
        self.assertEqual(self.amenity.name, "toor")
        self.assertIsInstance(self.amenity.name, str)
        self.assertEqual(dummy_instance.name, "")

    def test_save_method(self):
        """test save method"""
        dummy_instance = Amenity()
        dummy_instance.save()
        self.assertNotEqual(
            dummy_instance.created_at, dummy_instance.updated_at)

    def test_class_user(self):
        """ instance should be User; user should be subclass of BaseModel """
        self.assertTrue(issubclass(Amenity, BaseModel))
        self.assertIsInstance(self.amenity, Amenity)

    @classmethod
    def tearDownClass(cls):
        """clear everything"""
        del cls.amenity.name
        del cls.amenity

if __name__ == '__main__':
    unittest.main()
