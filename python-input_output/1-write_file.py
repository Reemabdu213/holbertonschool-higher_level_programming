#!/usr/bin/python3
"""Module for writing text to a file."""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF-8) and return number of characters.

    Args:
        filename (str): The name of the file to write to. Defaults to empty.
        text (str): The text to write to the file. Defaults to empty string.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
