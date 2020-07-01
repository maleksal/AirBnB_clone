#!/usr/bin/python3
"""
BaseModel Module
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    '''
    base model defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        """
        class constructor
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["updated_at", "created_at"]:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def __str__(self):
        '''
        returns a string reprisentation of the BaseModel class
        '''
        return "[{}] ({}) {}".format(
            type(self).__name__, self.id, self.__dict__)

    def save(self):
        '''
        updates the public instance attribute
        <updated_at> with the current datetime
        '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of self.__dict__.
        > adds (id, class name, updated_at, created_at) to dictionary
        '''
        hold_dictionary = {}
        for key, value in self.__dict__.items():
            if key in ["updated_at", "created_at"]:
                Pythoncode = "self.{}.isoformat()".format(key)
                hold_dictionary[key] = eval(Pythoncode)
            else:
                hold_dictionary[key] = value
        hold_dictionary["__class__"] = type(self).__name__
        return hold_dictionary
