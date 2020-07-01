#!/usr/bin/python3
"""
File storage Module
"""

import json
from models.base_model import BaseModel


class FileStorage():
    """
    FileStorage class serializes instances to a JSON
    file and deserializes JSON file to instances.

    Attributes:
        __file_path: string - path to the JSON file (ex: file.json)
        __objects: dictionary - will store all objects by <class name>.id

    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id.

        """
        key = "{}.{}".format(
                type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)

        """
        with open(self.__file_path, "w+") as file:
            new_dic = {}
            for key, obj in self.__objects.items():
                new_dic[key] = obj.to_dict()
            json.dump(new_dic, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        only if the JSON file (__file_path) exists ; otherwise
        do nothing If the file doesn’t exist, no exception should be raised.

        """
        try:
            with open(self.__file_path) as file:
                data = json.load(file)
            for obj_data in data.values():
                dummy_instance = eval(obj_data["__class__"])
                obj = dummy_instance(**obj_data)
                self.new(obj)
        except OSError:
            pass
