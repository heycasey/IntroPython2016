#!/usr/env/python3

import math

class Circle:

    def __init__(self, radius):
        self.radius = radius

        # self.diameter = radius * 2

    @property
    def diameter(self):
        return(self.radius * 2)

    @diameter.setter
    def diameter(self, val):
        self.radius = val / 2

    @property
    def area(self):
        return(self.radius**2 * math.pi)
