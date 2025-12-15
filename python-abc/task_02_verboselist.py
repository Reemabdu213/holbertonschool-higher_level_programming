#!/usr/bin/env python3
"""Module that defines VerboseList class"""


class VerboseList(list):
    """A list that prints notifications when modified"""

    def append(self, item):
        """
        Add an item to the list and print a notification

        Args:
            item: the item to add to the list
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        Extend the list with items from iterable and print a notification

        Args:
            iterable: an iterable of items to add to the list
        """
        items_count = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{items_count}] items.")

    def remove(self, item):
        """
        Remove an item from the list and print a notification

        Args:
            item: the item to remove from the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Pop an item from the list and print a notification

        Args:
            index: the index of the item to pop (default: -1, last item)

        Returns:
            The popped item
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
