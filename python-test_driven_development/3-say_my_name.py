#!/usr/bin/python3
"""
Module for printing names.
This module provides a function to print a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Prints 'My name is <first name> <last name>'.
    Both arguments must be strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
