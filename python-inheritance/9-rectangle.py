#!/usr/bin/python3
"""Module that defines a full Rectangle class based on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated private width and height."""

    def __init__(self, width, height):
        """Initialize a rectangle with a width and a height.

        Args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the description [Rectangle] <width>/<height>."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
