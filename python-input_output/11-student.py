#!/usr/bin/python3
"""Module defining a Student class."""


class Student:
    """Class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): Optional list of attribute names to retrieve.
                         If None, all attributes are retrieved.

        Returns:
            dict: Dictionary containing specified or all attributes.
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if hasattr(self, attr):
                result[attr] = getattr(self, attr)
        return result

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance.

        Args:
            json (dict): Dictionary with attribute names as keys
                        and their values.
        """
        for key, value in json.items():
            setattr(self, key, value)
