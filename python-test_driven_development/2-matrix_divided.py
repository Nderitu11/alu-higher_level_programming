#!/usr/bin/python3
"""2-matrix_divided module.

Provides matrix_divided(matrix, div) which divides every element of a
matrix (list of lists of integers/floats) by a number.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div, rounded to 2.

    Raise TypeError for an invalid matrix, rows of different sizes or a
    non-number div, and ZeroDivisionError if div is 0.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(msg)
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(item / div, 2) for item in row] for row in matrix]
