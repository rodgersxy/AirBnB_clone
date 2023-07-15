#!/usr/bin/python3
"""
Test cases for various aspects of City class
"""
import unittest
from models.city import City
from datetime import datetime
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    test City class
    """
    def setUp(self):
        """
        creates an instance of the City class and assigns
        it to the self.city attribute
        """
        self.city = City()

    def test_attribute_types(self):
        """
        To test the type of  city attribute
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)

    def test_inheritance(self):
        """
        to test if City inherits from BaseModel
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """
        To test the attributes if the City
        """
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_updated_at(self):
        """
        To test if updated_at attri is set to current time
        """
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_created_at(self):
        """
        To test if created _at attribute id set to current time
        """
        self.assertIsInstance(self.city.created_at, datetime)


if __name__ == "__main__":
    unittest.main()
