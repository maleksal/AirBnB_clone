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

    def test_class_method_all(self):
        """ Should return a dictionary datatype """
        my_model = FileStorage()
        holder = my_model.all()
        self.assertEqual(type(holder), dict)

    def test_class_method_new(self):
        """ Should sets in __objects the obj with key <obj class name>.id """
        my_model = FileStorage()
        dummy_instance = BaseModel()
        key = "BaseModel.{}".format(dummy_instance.id)
        dummy_instance.name = "testing"
        dummy_instance.number = 100
        my_model.new(dummy_instance)

        self.assertEqual(my_model.all()[key].name, "testing")
