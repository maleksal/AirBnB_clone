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
    """
    test FileStorage

    """

    def setUp(self):
        """ store FileStorage.objects & FileStorage.file_path """
        self.objects = FileStorage._FileStorage__objects
        self.file_path = FileStorage._FileStorage__file_path

    def test_object(self):
        """ test self.objects type """
        self.assertTrue(isinstance(self.objects, dict))

    def test_file_path(self):
        """ test type of file path """
        self.assertTrue(isinstance(self.file_path, str))

    def test_storage_type(self):
        """ <storage.all()> should be dictionary """
        storage = FileStorage()
        database = storage.all()
        self.assertEqual(type(database), dict)

    def test_method_new(self):
        """ test new method """
        storage = FileStorage()
        len_storage = len(storage.all())
        dummy_instance = BaseModel()
        storage.new(dummy_instance)
        self.assertTrue(len(storage.all()) == len_storage + 1)

    def test_method_reload(self):
        """ test reload method """
        storage = FileStorage()
        storage.reload()
        self.assertEqual(type(storage.all()), dict)

    def test_method_all(self):
        """ test all method """
        storage = FileStorage()

        self.assertEqual(type(storage.all()), dict)


class TestFileStorageBaseModel(unittest.TestCase):
    """ Test functionality of FileStorage in BaseModel """

    def setUp(self):
        """ setup BaseModel instance """
        self.storage = FileStorage()
        self.my_model = BaseModel()
        self.my_model.save()

    def test_base_model_update(self):
        """ BaseModel object shoud be added to FS objects """
        self.assertIn("BaseModel.{}".format(
            self.my_model.id), self.storage.all().keys())

if __name__ == '__main__':
    unittest.main()
