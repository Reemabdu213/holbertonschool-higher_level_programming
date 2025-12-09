#!/usr/bin/python3
"""Module that defines a Square class with private size attribute"""


class Square:
    """Class that defines a square with private size"""
    
    def __init__(self, size):
        """Initialize square with size
        
        Args:
            size: size of the square
        """
        self.__size = size
