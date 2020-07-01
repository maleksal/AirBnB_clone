#!/usr/bin/python3
""" test Review model """

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ test Review class"""
    @classmethod
    def setUp(cls):
        """steup class """
        cls.review = Review()
        cls.review.place_id = "1"
        cls.review.user_id = "2"
        cls.review.text = "toor"
        cls.review.save()

    def test_field_place_id(self):
        """ test first name field"""
        dummy_instance = Review()
        self.assertEqual(self.review.place_id, "1")
        self.assertIsInstance(self.review.place_id, str)
        self.assertEqual(dummy_instance.place_id, "")

    def test_field_user_id(self):
        """ test first name field"""
        dummy_instance = Review()
        self.assertEqual(self.review.user_id, "2")
        self.assertIsInstance(self.review.user_id, str)
        self.assertEqual(dummy_instance.user_id, "")

    def test_field_text(self):
        """ test first name field"""
        dummy_instance = Review()
        self.assertEqual(self.review.text, "toor")
        self.assertIsInstance(self.review.text, str)
        self.assertEqual(dummy_instance.text, "")

    def test_save_method(self):
        """test save method"""
        dummy_instance = Review()
        dummy_instance.save()
        self.assertNotEqual(
            dummy_instance.created_at, dummy_instance.updated_at)

    def test_class_user(self):
        """ instance should be User; user should be subclass of BaseModel """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, Review)

    @classmethod
    def tearDownClass(cls):
        """clear everything"""
        del cls.review.place_id
        del cls.review.user_id
        del cls.review.text
        del cls.review

if __name__ == '__main__':
    unittest.main()
