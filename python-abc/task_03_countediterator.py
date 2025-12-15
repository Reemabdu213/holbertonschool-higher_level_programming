#!/usr/bin/env python3
"""Module that defines CountedIterator class"""


class CountedIterator:
    """An iterator that keeps track of the number of items iterated"""

    def __init__(self, iterable):
        """
        Initialize a CountedIterator

        Args:
            iterable: any iterable object (list, tuple, etc.)
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself"""
        return self

    def __next__(self):
        """
        Fetch the next item and increment the counter

        Returns:
            The next item from the iterator

        Raises:
            StopIteration: when there are no more items
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        Get the number of items that have been iterated

        Returns:
            The current count
        """
        return self.count
