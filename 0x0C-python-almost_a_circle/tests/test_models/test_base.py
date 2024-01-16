#!/usr/bin/python3
import unittest
from models.base import Base
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests the Base class."""

    def setUp(self):
        """Imports module, instantiates class"""
        Base._Base__nb_objects = 0
        pass

    def tearDown(self):
        """Cleans up after each test_method."""
        pass
    
    def test_to_json_string_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_non_empty_list(self):
        input_list = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        expected_output = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        self.assertEqual(Base.to_json_string(input_list), expected_output)

    def test_from_json_string_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_from_json_string_non_empty_string(self):
        input_string = '[{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]'
        expected_output = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
        self.assertEqual(Base.from_json_string(input_string), expected_output)

    def test_save_to_file(self):
        obj_list = [Base(1), Base(2), Base(3)]
        Base.save_to_file(obj_list)
        with open("Base.json", "r") as file:
            content = file.read()
        self.assertEqual(content, '[{"id": 1}, {"id": 2}, {"id": 3}]')

    def test_create(self):
        dummy = Base.create(id=1, name="Alice")
        self.assertEqual(dummy.to_dictionary(), {'id': 1})

    def test_load_from_file(self):
        obj_list = [Base(1), Base(2), Base(3)]
        Base.save_to_file(obj_list)
        loaded_list = Base.load_from_file()
        self.assertEqual([obj.to_dictionary() for obj in loaded_list], [{'id': 1}, {'id': 2}, {'id': 3}])

if __name__ == "__main__":
    unittest.main()
