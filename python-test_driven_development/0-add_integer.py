#!/usr/bin/python3
"""
Module for adding two integers.
This module provides a function to add two numbers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats.
    Returns the sum as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
```

---

**ثالثاً: ملف الاختبار tests/0-add_integer.txt**
```
Test cases for add_integer function
====================================

Import the function:
    >>> add_integer = __import__('0-add_integer').add_integer

Test normal cases:
    >>> add_integer(1, 2)
    3

    >>> add_integer(100, -2)
    98

    >>> add_integer(2)
    100

Test with floats:
    >>> add_integer(100.3, -2)
    98

    >>> add_integer(5.5, 4.5)
    9

Test error cases:
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer

    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

    >>> add_integer("hello", 5)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
