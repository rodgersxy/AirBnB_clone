#!/usr/bin/python3

'''Module for base_model tests'''

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    '''Test Basemodel class'''
    def setup(self):
        '''Sets up test methods'''
        pass

    def tearDown(self):
        '''Tears down test method'''
        self.resetStorage()
        pass

    def test_init_with_attribute(self):
        '''A sample kwargs dict with attributes'''
        kwargs = {
                'name': 'John',
                'age': 35,
                'created_at': '2023-01-01T00:00:00',
                'updated_at': '2023-01-02T00:00:00'
        }
        instance = BaseModel(**kwargs)

        '''Check if attribute is set correctly'''
        self.assertEqual(instance.name, 'John')
        self.assertEqual(instance.age, 35)
        self.assertEqual(
            instance.created_at, datetime.fromisoformat('2023-01-01T00:00:00'))
        self.assertEqual(
            instance.updated_at, datetime.fromisoformat('2023-01-02T00:00:00'))

    def test_init_without_attributes(self):
        instance = BaseModel()

        '''Checks if attributes are set correctly'''
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)
        self.assertTrue(hasattr(models.storage, 'new'))

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(
            self.instance.id, self.instance.__dict__)
        self.assertEqual(str(self.instance), expected_str)

    def test_save_method(self):
        '''Save the initial updated_at value'''
        initial_updated_at = self.instance.updated_at

        '''Call the save method'''
        self.instance.save()

        '''Checks if the updated_at attributes is updated'''
        self.assertNotEqual(self.instance.updated_at, initial_updated_at)
        self.assertIsInstance(self.instance.updated_at, datetime)

        '''Checks if models.storage.save() is called'''
        self.assertTrue(models.storage.save.called)

    def test_to_dict_method(self):
        '''Set attribute values for instance'''
        self.instance.name = "John"
        self.instance.age = 35

        '''Call the to_dict method'''
        result = self.instance.to_dict()

        '''Check the keys in the returned dictionary'''
        self.assertIn("_class", result)
        self.assertIn("created_at", result)
        self.assertIn("updated_at", result)
        self.assertIn("name", result)
        self.assertIn("age", result)

        '''Check the value in the returned dictionary'''
        self.assertEqual(result["_class"], "BaseModel")
        self.assertIsInstance(result["created_at"], str)
        self.assertIsInstance(result["updated_at"], str)
        self.assertEqual(result["name"], "John")
        self.assertEqual(result["age"], 25)


if __name__ == '__main__':
    unittest.main()
