#!/usr/bin/python3
"""Module that prints a square with the character #"""


def print_square(size):
    """Prints a square with the character #

    Args:
        size: The size length of the square

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    # Check if size is an integer (but not a boolean)
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")

    # Check if size is negative
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print the square
    for i in range(size):
        print("#" * size)
