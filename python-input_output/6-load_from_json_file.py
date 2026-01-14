#!/usr/bin/python3
"""Module for loading Python objects from JSON files."""
import json


def load_from_json_file(filename):
    """
    Create an object from a JSON file.

    Args:
        filename (str): The name of the JSON file to read from.

    Returns:
        Python object represented by the JSON file contents.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
