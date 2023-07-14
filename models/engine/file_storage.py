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
    __objects = dict()


    classes = {
            "BaseModel": BaseModel,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
    }

    def __init__(self):
        """
        init method for FileStorage
        """
        pass

    def all(self):
        """
        method all conatain all the stored objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        new method adds new objecs to __objects dictionary
        converts it to dictionary using to_dict
        returns a unique key
        """
        dictionary = obj.to_dict()
        key = '{}.{}'.format(dictionary['__class__'], str(obj.id))
        FileStorage.__objects[key] = obj

    def save(self):
        """
        The save method serializes the objects stored in the
        __objects dictionary to a JSON file
        """
        dictionary = dict()
        for k, v in FileStorage.__objects.items():
            dictionary[k] = v.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(dictionary, file)

    def reload(self):
        """
        The reload method deserializes the JSON file and loads
        the data back into the __objects dictionary
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                json_load = json.load(file)
            for k, v in json_load.items():
                FileStorage.__objects[k] = BaseModel(**v)
        except FileNotFoundError:
            pass
