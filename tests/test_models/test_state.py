#!/usr/bin/python3
"""
unittest for user model
python3 -m unittest discover tests
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def setUp(self):
        """
        For State instances
        """
        self.state = State()

    def test_attributes(self):
        """
        To test the state attribute value
        """
        self.assertEqual(self.state.name, "")

    def test_str_representation(self):
        """
        To test the __str__ of State
        """
        expected_output = "[State] ({}) {}".format(
            self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_output)

    def test_save_method(self):
        """
        To test the save() method of State
        """
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(old_updated_at, self.state.updated_at)


if __name__ == '__main__':
    unittest.main()
