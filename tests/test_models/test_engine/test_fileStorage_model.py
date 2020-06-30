'''
Unittests Module for FileStorage class

'''
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    test FileStorage

    """

    def test_storage_obj(self):
        """ values in <storage.all()> should be class object """
        storage = FileStorage()
        for v in storage.all().values():
            self.assertTrue(v != dict)

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
