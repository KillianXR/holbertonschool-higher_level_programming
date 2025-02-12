#!/usr/bin/python3
"""
this module create a class of students with instances,
and retrieves a dictionary representation of a student instance
"""


class Student():
    """class creating"""

    def __init__(self, first_name, last_name, age):
        """
        class instances
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return dictionnary description of an object
        """
        if attrs is not None:
            return {name: value for name, value in self.__dict__.items()
                    if name in attrs}
        else:
            return self.__dict__
