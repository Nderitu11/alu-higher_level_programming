#!/usr/bin/python3
"""0-add_integer module.

Provides add_integer(a, b=98) which adds two integers or floats
after casting floats to integers.
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b (floats are cast first).
    Raise TypeError if a or b is not an integer or a float.
    """
    inf = float("inf")
    if not isinstance(a, (int, float)) or a != a or a in (inf, -inf):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or b != b or b in (inf, -inf):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
