#!/usr/bin/python3
"""
unittest for the review.py
Execute all tests: python3 -m unittest discover tests*
"""

import unittest
from models.base_model import BaseModel
from models.review import Review
import pep8
from datetime import datetime

class TestReview(unittest.TestCase):
    """
    To test  Review class
    """
    def setUp(self):
        """
        To create class instance
        """
        self.review = Review()

    def test_inheritance(self):
        """
        To test if Review inherits from BaseModel
        """
        self.assertTrue(issubclass(Review, BaseModel))
        self.assertIsInstance(self.review, BaseModel)

    def test_module_docstring(self):
        """
        To test doctstring
        """
        self.assertTrue(len(Review.__doc__) >= 1)

    def test_type_of_attributes(self):
        """
        To test the type of the attribute if its correct
        """
        self.assertIsInstance(self.review.text, str)
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)

    def test_updated_time(self):
        """
        To test the updated time of teh review after calling
        the save metho
        """
        review = Review()
        old_updated_at = review.updated_at
        review.save()
        new_updated_at = review.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIsInstance(new_updated_at, datetime)


if __name__ == '__main__':
    unittest.main()
