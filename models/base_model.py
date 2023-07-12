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
            for key, value in kwargs.item():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
	    self.created_at = datetime.now()
	    self.update_at = datetime.now()
	    models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
	Returns:
	    A string representation of the BaseModel instance in the
	    format:
	    [<class name>] (<self.id>) <self.__dict__>
	"""
	return("[{}] ({}) {}".format(
	    self.__class__.__name__, self.id, self.__dict__))
    
    def save(self):
        """
	updates the public instance attribute
	'updated_at' with the current datetime
	"""
	self.updated_at = datetime.now()
	models.storage.save()

    def to_dict(self):
        """
	Returns a dictionary representation of the BaseModel instance.
	Return-
	A dictionary containing all keys and values of the instance's
	__dict__ attribute.
	The dictionary will also include the '__class__' key with the
	class name of the object.
	The 'created_at' and 'updated_at' attributes are converted to
	string objects in ISO format.
	"""

	new_dict = self.__dict__.copy()
	new_dict["__class__"] = self.__class__.__name__
	new_dict["created_at"] = self.created_at.isoformat(sep='T')
	new_dict["updated_at"] = self.updated_at.isoformat(sep='T')


        return new_dict
