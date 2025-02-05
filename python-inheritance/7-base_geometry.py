#!/usr/bin/python3
"""
simple class
"""


class BaseGeometry:
    """create a class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if value is positive integer"""
        if type(value) is not int:
            raise TypeError(f"{str(name)} must be an integer")
        if value <= 0:
            raise ValueError(f"{str(name)} must be greater than 0")
