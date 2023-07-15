#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    test cases for Amenity
    """
    def setUp(self):
        """
        class instances
        """
        self.amenity = Amenity()

    def test_attributes(self):
        """
        To test if Amenity has name attribute
        """
        self.assertEqual(self.amenity.name, "")

    def test_inheritance(self):
        """
        To test if Amenity inherits fro the BaseModel class
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_save_method(self):
        """
        To test the save() method of Amenity and updates
        and update_at attri
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(old_updated_at, self.amenity.updated_at)

    def test_str_representation(self):
        """
        To test __str__ method of amenity class to ensure
        that is generated correctly
        """
        expected_output = "[Amenity] ({}) {}".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_output)

    def test_attribute_assignment_value(self):
        """
        To test if name attribute can be assigned a value
        """
        self.amenity.name = "Internet"
        self.assertEqual(self.amenity.name, "Internet")

    def tearDown(self):
        """clean up the instance"""
        del self.amenity

    def test_to_dict_method(self):
        """
        To test to_dict method of Amenity class to ensure that
        produces correct dictionary representation
        """
        obj_dict = self.amenity.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIn('created_at', obj_dict)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIn('updated_at', obj_dict)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'Amenity')


if __name__ == "__main__":
    unittest.main()
