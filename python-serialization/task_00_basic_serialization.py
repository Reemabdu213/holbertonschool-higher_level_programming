#!/usr/bin/python3
"""Module for basic serialization and deserialization using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
    """
    with open(filename, 'w') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Deserialize JSON data from a file to a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: Python dictionary with deserialized data.
    """
    with open(filename, 'r') as f:
        return json.load(f)
