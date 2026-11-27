#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_ordered_list(self):
        """Ascending list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max in the middle"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max at the beginning"""
        self.assertEqual(max_integer([9, 2, 3, 4]), 9)

    def test_max_at_end(self):
        """Max at the end"""
        self.assertEqual(max_integer([4, 3, 2, 10]), 10)

    def test_one_element(self):
        """List with one element"""
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        """Empty list returns None"""
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        """No argument returns None"""
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        """Only negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_signs(self):
        """Negative, zero and positive numbers"""
        self.assertEqual(max_integer([-1, 0, 1]), 1)

    def test_duplicates(self):
        """Repeated max value"""
        self.assertEqual(max_integer([3, 8, 8, 1]), 8)

    def test_all_equal(self):
        """All elements equal"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        """List of floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_int_and_float(self):
        """Mix of ints and floats"""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_tuple(self):
        """A tuple works as a sequence"""
        self.assertEqual(max_integer((1, 5, 3)), 5)

    def test_string(self):
        """A string is a sequence of characters"""
        self.assertEqual(max_integer("abc"), "c")

    def test_list_of_strings(self):
        """List of strings"""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_list_not_modified(self):
        """The list is left untouched"""
        lst = [3, 1, 2]
        max_integer(lst)
        self.assertEqual(lst, [3, 1, 2])

    def test_mixed_types(self):
        """Comparing int with str raises TypeError"""
        with self.assertRaises(TypeError):
            max_integer([1, "a"])

    def test_none(self):
        """None has no length"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_int_argument(self):
        """An int is not a sequence"""
        with self.assertRaises(TypeError):
            max_integer(5)

    def test_big_numbers(self):
        """Very large integers"""
        self.assertEqual(max_integer([10**20, 10**21, 5]), 10**21)
