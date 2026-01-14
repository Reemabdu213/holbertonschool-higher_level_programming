#!/usr/bin/python3
"""Module for converting Python objects to JSON strings."""
import json


def to_json_string(my_obj):
    """
    Return the JSON representation of an object (string).

    Args:
        my_obj: The Python object to convert to JSON string.

    Returns:
        str: JSON representation of the object.
    """
    return json.dumps(my_obj)
