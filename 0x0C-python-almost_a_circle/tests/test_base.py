#!/usr/bin/python3
"""
Unit tests for the base module
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    def test_A_nb_objects_private(self):
        '''Tests if nb_objects is private class attribute.'''
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))

    def test_default_id_increment(self):
        """Test defult inrement"""
        b1 = Base()
        b2 = Base()
        b3 = Base()

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_custom_id(self):
        """test custom"""
        b4 = Base(12)
        self.assertEqual(b4.id, 12)

    def test_default_id_after_custom_id(self):
        """Test default id after custom id"""
        Base._Base__nb_objects = 0  # Reset the counter for testing purposes
        b5 = Base()
        self.assertEqual(b5.id, 1)

    def test_to_json_string(self):
        """Test conversion to json string"""
        b = Base()
        json_string = Base.to_json_string([{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}])
        self.assertEqual(json_string, '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]')

    def test_to_json_string_empty_list(self):
        """Test emoty list"""
        json_string = Base.to_json_string([])
        self.assertEqual(json_string, '[]')

    def test_to_json_string_none(self):
        """Test None in to_json_string"""
        json_string = Base.to_json_string(None)
        self.assertEqual(json_string, '[]')

     def test_from_json_string(self):
         """Test from son string"""
        json_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        obj_list = Base.from_json_string(json_string)
        expected_list = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        self.assertEqual(obj_list, expected_list)

    def test_from_json_string_empty_string(self):
        """Test empty case in from_json_string"""
        obj_list = Base.from_json_string('')
        self.assertEqual(obj_list, [])

    def test_from_json_string_none(self):
        """Test None in from_json_string"""
        obj_list = Base.from_json_string(None)
        self.assertEqual(obj_list, [])

    def test_save_to_file(self):
        """Test save_to_file"""
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        with open('Base.json', 'r') as file:
            content = file.read()
        expected_content = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(content, expected_content)

    def test_save_to_file_empty_list(self):
        """Test empty list"""
        Base.save_to_file([])
        with open('Base.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')

    def test_save_to_file_none(self):
        """Test save_to_file"""
        Base.save_to_file(None)
        with open('Base.json', 'r') as file:
            content = file.read()
        self.assertEqual(content, '[]')

    def test_load_from_file(self):
        """Test load_from_file"""
        Base._Base__nb_objects = 0
        b1 = Base(1)
        b2 = Base(2)
        Base.save_to_file([b1, b2])
        loaded_list = Base.load_from_file()
        self.assertEqual(len(loaded_list), 2)
        self.assertEqual(loaded_list[0].id, 1)
        self.assertEqual(loaded_list[1].id, 2)

    def test_load_from_file_empty_file(self):
        """Test load_from_file"""
        Base._Base__nb_objects = 0
        with open('Base.json', 'w') as file:
            file.write('')
        loaded_list = Base.load_from_file()
        self.assertEqual(loaded_list, [])

    def test_load_from_file_nonexistent_file(self):
        """Test load rom file"""
        Base._Base__nb_objects = 0
        loaded_list = Base.load_from_file()
        self.assertEqual(loaded_list, [])

if __name__ == "__main__":
    unittest.main()

