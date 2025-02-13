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
        function that retrieves a dictionary representation of a Student
        (attrs: list of str only attribute name in this list must be retrives)
        """
        if attrs is None:
            return self.__dict__
        dictionary_2 = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary_2[key] = value
        return dictionary_2

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value) 