#!/usr/bin/python3
"""Module for appending text to a file."""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF-8).

    Args:
        filename (str): The name of the file to append to. Defaults to empty.
        text (str): The text to append to the file. Defaults to empty string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
