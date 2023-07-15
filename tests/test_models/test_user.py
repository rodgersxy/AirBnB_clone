#!/usr/bin/python3
"""
unittest module for user.py
To execute: python3 -m unittest discover tests
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    test case for User
    """
    def setUp(self):
        """
        To create instance class
        """
        self.user = User()

    def test_inheritance(self):
        """
        To test if user inherits from BaseModel
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        To test the attributs value
        """
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
