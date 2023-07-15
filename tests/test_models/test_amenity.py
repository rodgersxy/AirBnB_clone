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


if __name__ == "__main__":
    unittest.main()
