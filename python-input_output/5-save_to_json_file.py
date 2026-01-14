#!/usr/bin/python3
"""Module for saving Python objects to JSON files."""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using a JSON representation.

    Args:
        my_obj: The Python object to serialize and save.
        filename (str): The name of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
