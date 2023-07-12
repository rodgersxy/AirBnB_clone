#!/usr/bin/python3

'''Module for all base_model tests cases'''

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

if __name__ == '__main__':
    unittest.main()
