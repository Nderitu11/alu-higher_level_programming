#!/usr/bin/python3
"""Unittests for the Rectangle class."""
import io
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

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
        self.assertTrue(len(__import__("models.rectangle").rectangle
                            .__doc__) > 10)
        self.assertTrue(len(Rectangle.__doc__) > 10)
        for name in ("__init__", "area", "display", "__str__", "update",
                     "to_dictionary"):
            self.assertTrue(len(getattr(Rectangle, name).__doc__) > 10)
        for name in ("width", "height", "x", "y"):
            prop = getattr(Rectangle, name)
            self.assertTrue(len(prop.fget.__doc__) > 10)
            self.assertTrue(len(prop.fset.__doc__) > 10)

    def test_inheritance(self):
        """Rectangle inherits from Base."""
        self.assertIsInstance(Rectangle(1, 1), Base)

    def test_ids(self):
        """Ids are automatic or given."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """Getters return the given values."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))

    def test_defaults(self):
        """x and y default to 0."""
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private(self):
        """Attributes are stored privately."""
        r = Rectangle(1, 2, 3, 4)
        self.assertEqual(r._Rectangle__width, 1)
        self.assertEqual(r._Rectangle__height, 2)
        self.assertEqual(r._Rectangle__x, 3)
        self.assertEqual(r._Rectangle__y, 4)
        self.assertNotIn("width", r.__dict__)

    def test_missing_args(self):
        """Width and height are mandatory."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_too_many_args(self):
        """Too many arguments raise TypeError."""
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_width_type(self):
        """A non integer width raises TypeError."""
        for bad in ("2", 2.5, None, True, [1], {}, (1,), {1}):
            with self.assertRaises(TypeError) as cm:
                Rectangle(bad, 2)
            self.assertEqual(str(cm.exception), "width must be an integer")

    def test_height_type(self):
        """A non integer height raises TypeError."""
        for bad in ("2", 2.5, None, True, [1], {}):
            with self.assertRaises(TypeError) as cm:
                Rectangle(1, bad)
            self.assertEqual(str(cm.exception), "height must be an integer")

    def test_x_type(self):
        """A non integer x raises TypeError."""
        for bad in ("2", 2.5, None, True, [1], {}):
            with self.assertRaises(TypeError) as cm:
                Rectangle(1, 2, bad)
            self.assertEqual(str(cm.exception), "x must be an integer")

    def test_y_type(self):
        """A non integer y raises TypeError."""
        for bad in ("2", 2.5, None, True, [1], {}):
            with self.assertRaises(TypeError) as cm:
                Rectangle(1, 2, 3, bad)
            self.assertEqual(str(cm.exception), "y must be an integer")

    def test_width_value(self):
        """A width of 0 or less raises ValueError."""
        for bad in (0, -1, -100):
            with self.assertRaises(ValueError) as cm:
                Rectangle(bad, 2)
            self.assertEqual(str(cm.exception), "width must be > 0")

    def test_height_value(self):
        """A height of 0 or less raises ValueError."""
        for bad in (0, -1, -100):
            with self.assertRaises(ValueError) as cm:
                Rectangle(1, bad)
            self.assertEqual(str(cm.exception), "height must be > 0")

    def test_x_value(self):
        """A negative x raises ValueError and 0 is accepted."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 2, -1)
        self.assertEqual(str(cm.exception), "x must be >= 0")
        self.assertEqual(Rectangle(1, 2, 0).x, 0)

    def test_y_value(self):
        """A negative y raises ValueError and 0 is accepted."""
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 2, 3, -1)
        self.assertEqual(str(cm.exception), "y must be >= 0")
        self.assertEqual(Rectangle(1, 2, 3, 0).y, 0)

    def test_validation_order(self):
        """Width is validated before the other attributes."""
        with self.assertRaises(TypeError) as cm:
            Rectangle("a", "b", "c", "d")
        self.assertEqual(str(cm.exception), "width must be an integer")
        with self.assertRaises(ValueError) as cm:
            Rectangle(-1, "b")
        self.assertEqual(str(cm.exception), "width must be > 0")
        with self.assertRaises(TypeError) as cm:
            Rectangle(1, "b")
        self.assertEqual(str(cm.exception), "height must be an integer")
        with self.assertRaises(ValueError) as cm:
            Rectangle(1, 1, -1, "d")
        self.assertEqual(str(cm.exception), "x must be >= 0")

    def test_setters(self):
        """Setters change and validate the attributes."""
        r = Rectangle(1, 2)
        r.width = 10
        r.height = 20
        r.x = 3
        r.y = 4
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 3, 4))
        with self.assertRaises(ValueError):
            r.width = -10
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(TypeError):
            r.y = "1"
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 3, 4))

    def test_big_values(self):
        """Very large integers are accepted."""
        self.assertEqual(Rectangle(10 ** 20, 10 ** 20).area(), 10 ** 40)

    def test_area(self):
        """Area is width times height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        self.assertEqual(Rectangle(1, 1).area(), 1)

    def test_area_args(self):
        """area takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display(self):
        """display prints the rectangle."""
        self.assertEqual(self.output(Rectangle(4, 2).display),
                         "####\n####\n")
        self.assertEqual(self.output(Rectangle(1, 1).display), "#\n")

    def test_display_xy(self):
        """display uses x and y."""
        self.assertEqual(self.output(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(self.output(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")
        self.assertEqual(self.output(Rectangle(1, 1, 0, 1).display),
                         "\n#\n")

    def test_display_args(self):
        """display takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).display(1)

    def test_str(self):
        """__str__ has the expected format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_print(self):
        """print uses __str__."""
        out = self.output(lambda: print(Rectangle(1, 2, 3, 4, 5)))
        self.assertEqual(out, "[Rectangle] (5) 3/4 - 1/2\n")

    def test_update_args(self):
        """update assigns positional arguments in order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 10/10")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/10 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_extra_args(self):
        """Extra positional arguments are ignored."""
        r = Rectangle(1, 1)
        r.update(5, 2, 3, 4, 5, 6, 7)
        self.assertEqual(str(r), "[Rectangle] (5) 4/5 - 2/3")

    def test_update_none_id(self):
        """update can set the id to None."""
        r = Rectangle(1, 1)
        r.update(None)
        self.assertIsNone(r.id)

    def test_update_no_args(self):
        """update without arguments changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_kwargs(self):
        """update assigns keyword arguments in any order."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(2, width=50)
        self.assertEqual(str(r), "[Rectangle] (2) 0/0 - 1/1")

    def test_update_unknown_kwargs(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 1, 0, 0, 1)
        r.update(foo=1, size=5)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        self.assertFalse(hasattr(r, "foo"))

    def test_update_invalid(self):
        """update validates values."""
        r = Rectangle(1, 1)
        with self.assertRaises(TypeError):
            r.update(1, "a")
        with self.assertRaises(ValueError):
            r.update(1, 2, 3, -1)
        with self.assertRaises(ValueError):
            r.update(width=0)
        with self.assertRaises(TypeError):
            r.update(y="y")

    def test_to_dictionary(self):
        """to_dictionary returns all the attributes."""
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"id": 1, "width": 10, "height": 2,
                             "x": 1, "y": 9})

    def test_to_dictionary_update(self):
        """A dictionary can be passed to update."""
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertFalse(r1 == r2)

    def test_to_dictionary_args(self):
        """to_dictionary takes no argument."""
        with self.assertRaises(TypeError):
            Rectangle(1, 1).to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
