#!/usr/bin/python3
"""
The module is the base of all the classes
"""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
    BaseModel that defines common attributs and mothods
    for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        To initialize BaseModel
        Args - *args: Variable length argument list (not used)
        **kwargs: Keyword arguments containing attribute values
        The 'keys' represent attribute names, and the values represent
        attribute values.
        """

        if kwargs:
            self.updated_at = datetime.\
                strptime(kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            self.created_at = datetime.\
                strptime(kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            for k, v in kwargs.items():
                if k not in ['updated_at', 'created_at', '__class__']:
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        Returns:
            A string representation of the BaseModel instance in the
            format:
            [<class name>] (<self.id>) <self.__dict__>
        """
        return '[{}] ({}) {}'\
            .format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel instance.
        Return-:
        A dictionary containing all keys and values of the instance's
        __dict__ attribute.
        The dictionary will also include the '__class__' key with the
        class name of the object.
        The 'created_at' and 'updated_at' attributes are converted to
        string objects in ISO format.
        """

        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()

        return new_dict
