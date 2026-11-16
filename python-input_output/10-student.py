#!/usr/bin/python3
"""Module that defines a Student class with a filtered to_json."""


class Student:
    """Defines a student by first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student.

        Args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        Args:
            attrs (list): attribute names to keep. If it is not a list
                of strings, all attributes are returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(a, str) for a in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
