#!/usr/bin/python3
"""
Public instance return true if (obj) is exactly,
an instance of a specified class else return false
"""


def is_same_class(obj, a_class):
    """
    Public instance return true if (obj) is exactly,
    an instance of a specified class else retrun false
    """
    if type(obj) is a_class:
        return True
    else:
        return False
