#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_list(self):
        """Test with a normal list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with only one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_max_at_beginning(self):
        """Test when max is at the beginning"""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test when max is at the end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_max_in_middle(self):
        """Test when max is in the middle"""
        self.assertEqual(max_integer([1, 10, 3, 4]), 10)

    def test_negative_numbers(self):
        """Test with negative numbers"""
        self.assertEqual(max_integer([-1, -5, -3, -2]), -1)

    def test_positive_and_negative(self):
        """Test with positive and negative numbers"""
        self.assertEqual(max_integer([-1, 5, -3, 2]), 5)

    def test_all_same(self):
        """Test when all elements are the same"""
        self.assertEqual(max_integer([7, 7, 7, 7]), 7)

    def test_floats(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.5, 2.7, 3.2, 1.8]), 3.2)

    def test_ints_and_floats(self):
        """Test with integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 1.8]), 3)


if __name__ == '__main__':
    unittest.main()
