#!/usr/bin/python3
"""
BaseModel Module
"""

from uuid import uuid4
from datetime import datetime


class BaseModel:
    '''
    base model defines all common attributes/methods for other classes
    '''

    def __init__(self, *args, **kwargs):
        """
        class constructor
        """
        if kwargs is not {}:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

            for key, value in kwargs.items():
                if key != "__class__":
                    if value in [kwargs["updated_at"], kwargs["created_at"]]:
                        value = datetime.strptime(
                            value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()

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

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of self.__dict__.
        > adds (id, class name, updated_at, created_at) to dictionary
        '''
        dictionary = self.__dict__
        dictionary["id"] = str(self.id)
        dictionary["__class__"] = type(self).__name__
        dictionary["updated_at"] = str(self.updated_at.isoformat())
        dictionary["created_at"] = str(self.created_at.isoformat())

        return dictionary
