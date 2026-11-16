#!/usr/bin/python3
"""Module that defines MyList, a list that can print itself sorted."""


class MyList(list):
    """A list subclass with an extra method to print it sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
