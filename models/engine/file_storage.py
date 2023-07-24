#!/usr/bin/python3
"""
FileStorage class provides methods for storing, retrieving,
and saving objects to/from a JSON file.
"""


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class FileStorage has two private class attributes
    __file_path: repre path to JSON file
    __objects: repre dictionary to represent to store objects
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        method all conatain all the stored objects
        """
        return self.__objects

    def new(self, obj):
        """
        new method adds new objecs to __objects dictionary
        converts it to dictionary using to_dict
        returns a unique key
        """
        self.__objects.update({f"{obj.__class__.__name__}.{obj.id}": obj})

    def save(self):
        """
        The save method serializes the objects stored in the
        __objects dictionary to a JSON file
        """
        dictionary = dict()
        for key, value in self.__objects.items():
            dictionary[k] = v.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file, indent=2)

    def reload(self):
        """
        The reload method deserializes the JSON file and loads
        the data back into the __objects dictionary
        """
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as fd:
                dict_json = json.load(fd)
                for key, value in dict_json.items():
                    self.__objects[key] = eval(value['__class__'])(**value)
        except FileNotFoundError:
            pass
