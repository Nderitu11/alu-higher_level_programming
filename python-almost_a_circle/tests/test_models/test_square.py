#!/usr/bin/python3
"""Unittests for the Square class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the id counter."""
        Base._Base__nb_objects = 0

    @staticmethod
    def output(func):
        """Return everything printed by func."""
        with patch("sys.stdout", new_callable=io.StringIO) as out:
            func()
        return out.getvalue()

    def test_docs(self):
        """Module, class and methods are documented."""
        self.assertTrue(len(__import__("models.square").square
                            .__doc__) > 10)
        self.assertTrue(len(Square.__doc__) > 10)
        for name in ("__init__", "__str__", "update", "to_dictionary"):
            self.assertTrue(len(getattr(Square, name).__doc__) > 10)
        self.assertTrue(len(Square.size.fget.__doc__) > 10)
        self.assertTrue(len(Square.size.fset.__doc__) > 10)

    def test_inheritance(self):
        """Square inherits from Rectangle and Base."""
        s = Square(1)
        self.assertIsInstance(s, Rectangle)
        self.assertIsInstance(s, Base)

    def test_init(self):
        """Square sets size, position and id."""
        s = Square(5)
        self.assertEqual((s.size, s.width, s.height, s.x, s.y, s.id),
                         (5, 5, 5, 0, 0, 1))
        s = Square(2, 3, 4, 9)
        self.assertEqual((s.size, s.x, s.y, s.id), (2, 3, 4, 9))
        self.assertEqual(Square(1).id, 2)

    def test_no_new_attributes(self):
        """Square uses the attributes of Rectangle only."""
        self.assertEqual(sorted(Square(1).__dict__),
                         ["_Rectangle__height", "_Rectangle__width",
                          "_Rectangle__x", "_Rectangle__y", "id"])

    def test_missing_args(self):
        """Size is mandatory."""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """Too many arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_size_type(self):
        """A non integer size raises TypeError about width."""
        for bad in ("2", 2.5, None, True, [1], {}):
            with self.assertRaises(TypeError) as cm:
                Square(bad)
            self.assertEqual(str(cm.exception), "width must be an integer")

    def test_size_value(self):
        """A size of 0 or less raises ValueError about width."""
        for bad in (0, -1):
            with self.assertRaises(ValueError) as cm:
                Square(bad)
            self.assertEqual(str(cm.exception), "width must be > 0")

    def test_xy_validation(self):
        """x and y are validated like in Rectangle."""
        with self.assertRaises(TypeError) as cm:
            Square(1, "a")
        self.assertEqual(str(cm.exception), "x must be an integer")
        with self.assertRaises(TypeError) as cm:
            Square(1, 0, "a")
        self.assertEqual(str(cm.exception), "y must be an integer")
        with self.assertRaises(ValueError) as cm:
            Square(1, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")
        with self.assertRaises(ValueError) as cm:
            Square(1, 0, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")

    def test_size_setter(self):
        """The size setter changes width and height."""
        s = Square(5)
        s.size = 10
        self.assertEqual((s.size, s.width, s.height), (10, 10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_setter_invalid(self):
        """The size setter validates the value."""
        s = Square(5)
        with self.assertRaises(TypeError) as cm:
            s.size = "9"
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            s.size = 0
        self.assertEqual(str(cm.exception), "width must be > 0")
        self.assertEqual(s.size, 5)

    def test_area(self):
        """Area is size squared."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(Square(2, 2).area(), 4)
        self.assertEqual(Square(3, 1, 3).area(), 9)

    def test_display(self):
        """display prints the square with x and y."""
        self.assertEqual(self.output(Square(2).display), "##\n##\n")
        self.assertEqual(self.output(Square(2, 2).display),
                         "  ##\n  ##\n")
        self.assertEqual(self.output(Square(1, 1, 2).display),
                         "\n\n #\n")

    def test_str(self):
        """__str__ has the expected format."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3, 8)), "[Square] (8) 1/3 - 3")

    def test_update_args(self):
        """update assigns positional arguments in order."""
        s = Square(5)
        s.update(10)
        self.assertEqual(str(s), "[Square] (10) 0/0 - 5")
        s.update(1, 2)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 2")
        s.update(1, 2, 3)
        self.assertEqual(str(s), "[Square] (1) 3/0 - 2")
        s.update(1, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_extra_args(self):
        """Extra positional arguments are ignored."""
        s = Square(5)
        s.update(1, 2, 3, 4, 5, 6)
        self.assertEqual(str(s), "[Square] (1) 3/4 - 2")

    def test_update_kwargs(self):
        """update assigns keyword arguments."""
        s = Square(5)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/0 - 5")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        s = Square(5)
        s.update(3, size=50)
        self.assertEqual(str(s), "[Square] (3) 0/0 - 5")

    def test_update_unknown_kwargs(self):
        """Unknown keys are ignored."""
        s = Square(5)
        s.update(foo=1, width=9)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_update_no_args(self):
        """update without arguments changes nothing."""
        s = Square(5, 1, 2, 3)
        s.update()
        self.assertEqual(str(s), "[Square] (3) 1/2 - 5")

    def test_update_invalid(self):
        """update validates values."""
        s = Square(5)
        with self.assertRaises(TypeError):
            s.update(1, "a")
        with self.assertRaises(ValueError):
            s.update(1, 2, -1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(TypeError):
            s.update(y="a")

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 1, "size": 10, "x": 2, "y": 1})

    def test_to_dictionary_update(self):
        """A dictionary can be passed to update."""
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertFalse(s1 == s2)

    def test_to_dictionary_args(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Square(1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
