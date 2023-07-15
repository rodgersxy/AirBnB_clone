#!/usr/bin/python3

'''Module for all base_model tests cases'''
import pep8
import time
import unittest
from uuid import UUID, uuid4
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Test Basemodel class'''
    def setUp(self):
        '''Sets up test methods'''
        self.instance = BaseModel

    def tearDown(self):
        '''Tears down the method'''
        del self.instance

    def test_init_with_attribute(self):
        '''A sample kwargs dict with attributes'''
        kwargs = {
                'name': 'John',
                'age': 35,
                'created_at': '2023-01-01T00:00:00.000000',
                'updated_at': '2023-01-02T00:00:00.000000'
        }
        instance = BaseModel(**kwargs)

        '''Check if attribute is set correctly'''
        self.assertEqual(instance.name, 'John')
        self.assertEqual(instance.age, 35)
        self.assertEqual(
            instance.created_at, datetime(2023, 1, 1, 0, 0, 0))
        self.assertEqual(
            instance.updated_at, datetime(2023, 1, 2, 0, 0, 0))

    def test_str_representation(self):
        '''Test __str__ representation'''
        self.instance = BaseModel()
        str_repr = str(self.instance)

        expected_str = "[BaseModel] ({}) {}".format(
            self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), expected_str)

    def test_save_method(self):
        """
        To test that the save method updates the updated_at attribute
        and also saves the object
        """
        base_model = BaseModel()
        old_updated_at = base_model.updated_at
        base_model.save()
        new_updated_at = base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertIsInstance(new_updated_at, datetime)

    def test_unique_ids(self):
        """
        to test that BaseModel instances has unique ids
        """
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertIsInstance(base_model_1.id, str)
        self.assertIsInstance(base_model_2.id, str)
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_to_dict(self):
        """
        To test to_dict method to ensure the correct conversion
        """
        base_model = BaseModel()
        obj_dict = base_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIsInstance(obj_dict['id'], str)
        self.assertIn('created_at', obj_dict)
        self.assertIsInstance(obj_dict['created_at'], str)
        self.assertIn('updated_at', obj_dict)
        self.assertIsInstance(obj_dict['updated_at'], str)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_pep8_conformance(self):
        """
        To Test that the BaseModel class conforms to PEP 8.
        """
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(
            result.total_errors, 0, "PEP 8 style violations found")

    def test_docstring_exists(self):
        """
        To test if docstring exists in BaseMOdel class
        """
        self.assertIsNotNone(BaseModel.__doc__)


if __name__ == '__main__':
    unittest.main()
