#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """Class that inherits from list with additional method"""

    def print_sorted(self):
        """Prints the list in ascending sorted order"""
        print(sorted(self))
