#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity


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


if __name__ == "__main__":
    unittest.main()
