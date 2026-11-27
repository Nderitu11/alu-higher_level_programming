#!/usr/bin/python3
"""Module that defines the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Class that represents a rectangle and inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a rectangle with a size, a position and an id."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate(name, value, minimum):
        """Raise an error if value is not an integer of at least minimum."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value < minimum:
            if minimum == 0:
                raise ValueError("{} must be >= 0".format(name))
            raise ValueError("{} must be > 0".format(name))

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width after checking it is an integer greater than 0."""
        self._validate("width", value, 1)
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height after checking it is an integer greater than 0."""
        self._validate("height", value, 1)
        self.__height = value

    @property
    def x(self):
        """Get the x coordinate of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set x after checking it is an integer greater or equal to 0."""
        self._validate("x", value, 0)
        self.__x = value

    @property
    def y(self):
        """Get the y coordinate of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set y after checking it is an integer greater or equal to 0."""
        self._validate("y", value, 0)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with the character # using x and y offsets."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return the string [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from positional arguments or else keywords."""
        if args:
            names = ["id", "width", "height", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
            return
        for name, value in kwargs.items():
            if name in ("id", "width", "height", "x", "y"):
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
