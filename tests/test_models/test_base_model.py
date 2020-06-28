import unittest
from models.base_model import BaseModel
'''
Unittests Module
'''


class TestBaseModel(unittest.TestCase):
    """
    test BaseModel
    
    """
    
    def test_class_constructor_0(self):
        """
        test class constructor without kwargs (id, created_at) should be created
        
        """
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)

    def test_class_constructor_1(self):
        """
        Test class constructor with kwargs:
        (id, created_at, updated_at, name, number) should be created
        
        """
        # template model
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        
        # new model
        my_new_model = BaseModel(**my_model_json)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.name)
        self.assertIsNotNone(my_model.my_number)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)
        
    def test_uuid(self):
        """
        test if uuid is different for two indentical objects
        
        """
        
        # Model 1
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        
        # Model 2
        my_model_2 = BaseModel()
        my_model_2.name = "Holberton"
        my_model_2.my_number = 89
        
        self.assertNotEqual(my_model.id, my_model_2.id)

    
    def test_to_dictionaryMethod(self):
        """ test if <to_dictionary> method returns a dict datatype"""
        my_model = BaseModel()
        my_model.name = "Holberton"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()
        self.assertEqual(type(my_model_json), dict)
    
    def test_saveMethod(self):
        """ test save method that updates time for <updated_at """
        my_model = BaseModel()
        old_time = my_model.updated_at
        my_model.save() # update time
        new_time = my_model.updated_at
        self.assertNotEqual(old_time, new_time)