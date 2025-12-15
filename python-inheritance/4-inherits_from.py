#!/usr/bin/python3
"""Module that defines inherits_from function"""


def inherits_from(obj, a_class):
    """
    Returns True if obj is an instance of a class that inherited from a_class

    Args:
        obj: The object to check
        a_class: The class to compare with

    Returns:
        True if obj is an instance of a subclass of a_class
        False if obj is exactly an instance of a_class or not related
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
