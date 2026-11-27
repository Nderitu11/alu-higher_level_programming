#!/usr/bin/python3
"""Module that defines the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that represents a square and inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a square with a size, a position and an id."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the width and the height of the square to the same value."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the string [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes from positional arguments or else keywords."""
        if args:
            names = ["id", "size", "x", "y"]
            for name, value in zip(names, args):
                setattr(self, name, value)
            return
        for name, value in kwargs.items():
            if name in ("id", "size", "x", "y"):
                setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
