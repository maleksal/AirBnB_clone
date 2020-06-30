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
        """ <storage.all()> should be object """
        storage = FileStorage()
        for v in storage.all().values():
            self.assertTrue(v != dict)
