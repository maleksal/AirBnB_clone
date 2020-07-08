#!/usr/bin/python3
'''
Unittests Module for FileStorage class

'''
import unittest
import inspect
import pep8
import pycodestyle
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """ Unittests"""

    @classmethod
    def setUp(cls):
        """steup class"""
        cls.storage = FileStorage()
        cls.dummy_instance = BaseModel()

    def test_instance(self):
        """ instance type should be FileStorage"""
        self.assertIsInstance(self.storage, FileStorage)
        self.assertEqual(type(self.storage), FileStorage)

    def test_method_save(self):
        """test FileStorage save method"""
        self.storage.new(self.dummy_instance)
        self.storage.save()
        self.assertIsInstance(self.storage._FileStorage__objects, dict)

    def test_method_all(self):
        """storage.all() should be dict"""
        store = self.storage.all()
        self.assertIsInstance(store, dict)

    def test_method_new(self):
        """ test FileStorage new method """
        key = "BaseModel.{}".format(self.dummy_instance.id)
        self.storage.new(self.dummy_instance)
        self.assertEqual(self.dummy_instance, self.storage.all()[key])

    def test_method_realod(self):
        """ test FileStorage reload method"""
        self.assertFalse(self.storage.reload())
        os.remove("file.json")
        self.assertRaises(FileNotFoundError, self.storage.reload())

    def test_FileStorage_doc(self):
        """test for docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)

    def test_FileStorage_methods_doc(self):
        """test for docstrings"""
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_base_model_save(self):
        dummy_instance = BaseModel()
        dummy_instance.save()

    @classmethod
    def tearDown(cls):
        """clear everything"""
        del cls.storage
        del cls.dummy_instance

if __name__ == '__main__':
    unittest.main()
