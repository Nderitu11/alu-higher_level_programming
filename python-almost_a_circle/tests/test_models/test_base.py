#!/usr/bin/python3
"""Unittests for the Base class."""
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Test cases for the Base class."""

    def setUp(self):
        """Reset the id counter and remove old JSON files."""
        Base._Base__nb_objects = 0
        self.remove_files()

    def tearDown(self):
        """Remove the JSON files created by the tests."""
        self.remove_files()

    @staticmethod
    def remove_files():
        """Delete the JSON files used by the tests if they exist."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def read(self, name):
        """Return the content of a file."""
        with open(name, "r") as file:
            return file.read()

    def test_docs(self):
        """Module, class and methods are documented."""
        self.assertTrue(len(__import__("models.base").base.__doc__) > 10)
        self.assertTrue(len(Base.__doc__) > 10)
        for name in ("__init__", "to_json_string", "save_to_file",
                     "from_json_string", "create", "load_from_file"):
            self.assertTrue(len(getattr(Base, name).__doc__) > 10)

    def test_auto_ids(self):
        """Ids are incremented automatically."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base().id, 3)

    def test_given_id(self):
        """A given id is kept and does not change the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)

    def test_odd_ids(self):
        """Any non None id is assigned as is."""
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base("abc").id, "abc")
        self.assertEqual(Base(2.5).id, 2.5)
        self.assertEqual(Base().id, 1)

    def test_none_id(self):
        """An explicit None id means automatic id."""
        self.assertEqual(Base(None).id, 1)

    def test_two_args(self):
        """Too many arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_private_counter(self):
        """The counter is a private class attribute."""
        Base()
        self.assertEqual(Base._Base__nb_objects, 1)
        self.assertFalse(hasattr(Base, "__nb_objects"))

    def test_to_json_string_none(self):
        """None gives an empty list string."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """An empty list gives an empty list string."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_one(self):
        """One dictionary is converted."""
        res = Base.to_json_string([{"id": 1}])
        self.assertIsInstance(res, str)
        self.assertEqual(res, '[{"id": 1}]')

    def test_to_json_string_many(self):
        """Several dictionaries are converted."""
        data = [{"id": 1, "x": 2}, {"id": 3, "y": 4}]
        self.assertEqual(Base.from_json_string(
            Base.to_json_string(data)), data)

    def test_to_json_string_args(self):
        """Wrong number of arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_save_rectangles(self):
        """Rectangles are saved in Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertEqual(Base.from_json_string(self.read("Rectangle.json")),
                         [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_squares(self):
        """Squares are saved in Square.json."""
        s1 = Square(5)
        Square.save_to_file([s1])
        self.assertEqual(Base.from_json_string(self.read("Square.json")),
                         [s1.to_dictionary()])

    def test_save_none(self):
        """None saves an empty list."""
        Rectangle.save_to_file(None)
        self.assertEqual(self.read("Rectangle.json"), "[]")
        Square.save_to_file(None)
        self.assertEqual(self.read("Square.json"), "[]")
        Base.save_to_file(None)
        self.assertEqual(self.read("Base.json"), "[]")

    def test_save_empty(self):
        """An empty list saves an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(self.read("Rectangle.json"), "[]")

    def test_save_overwrite(self):
        """An existing file is overwritten."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        self.assertEqual(len(Base.from_json_string(
            self.read("Rectangle.json"))), 1)

    def test_save_args(self):
        """Wrong number of arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])

    def test_from_json_string_none(self):
        """None gives an empty list."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """An empty string gives an empty list."""
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """A JSON string gives a list of dictionaries."""
        res = Base.from_json_string('[{"id": 89, "width": 10}]')
        self.assertIsInstance(res, list)
        self.assertEqual(res, [{"id": 89, "width": 10}])

    def test_from_json_string_args(self):
        """Wrong number of arguments raises TypeError."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_create_rectangle(self):
        """create builds an equal but different Rectangle."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_create_square(self):
        """create builds an equal but different Square."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertIsInstance(s2, Square)
        self.assertIsNot(s1, s2)
        self.assertEqual(str(s1), str(s2))

    def test_create_partial(self):
        """create works with only some attributes."""
        r = Rectangle.create(id=5, width=4, height=3)
        self.assertEqual(str(r), "[Rectangle] (5) 0/0 - 4/3")

    def test_create_invalid(self):
        """create validates the values."""
        with self.assertRaises(ValueError):
            Rectangle.create(width=-1)

    def test_load_missing(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_rectangles(self):
        """Rectangles are loaded from their file."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        res = Rectangle.load_from_file()
        self.assertEqual(len(res), 2)
        self.assertIsInstance(res[0], Rectangle)
        self.assertIsNot(res[0], r1)
        self.assertEqual(str(res[0]), str(r1))
        self.assertEqual(str(res[1]), str(r2))

    def test_load_squares(self):
        """Squares are loaded from their file."""
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        res = Square.load_from_file()
        self.assertEqual([str(s) for s in res], [str(s1), str(s2)])
        self.assertIsInstance(res[1], Square)

    def test_load_empty_file(self):
        """A file with an empty list gives an empty list."""
        Rectangle.save_to_file([])
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_args(self):
        """Extra arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(1)


if __name__ == "__main__":
    unittest.main()
