#!/usr/bin/env python3
"""Module that demonstrates multiple inheritance with Fish and Bird classes"""


class Fish:
    """Fish class with swim and habitat methods"""

    def swim(self):
        """Print that the fish is swimming"""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat"""
        print("The fish lives in water")


class Bird:
    """Bird class with fly and habitat methods"""

    def fly(self):
        """Print that the bird is flying"""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat"""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class that inherits from both Fish and Bird"""

    def swim(self):
        """Override swim method"""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly method"""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat method"""
        print("The flying fish lives both in water and the sky!")
