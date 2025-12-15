#!/usr/bin/env python3
"""Module that demonstrates mixins with SwimMixin and FlyMixin"""


class SwimMixin:
    """Mixin that adds swimming ability"""

    def swim(self):
        """Make the creature swim"""
        print("The creature swims!")


class FlyMixin:
    """Mixin that adds flying ability"""

    def fly(self):
        """Make the creature fly"""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can swim, fly, and roar"""

    def roar(self):
        """Make the dragon roar"""
        print("The dragon roars!")
