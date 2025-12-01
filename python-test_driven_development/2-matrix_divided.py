#!/usr/bin/python3
"""
Module for dividing matrix elements.
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Returns a new matrix with results rounded to 2 decimal places.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_length = None
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")

        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of "
                    "integers/floats")

        if row_length is None:
            row_length = len(row)
        elif len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    return [[round(element / div, 2) for element in row] for row in matrix]
