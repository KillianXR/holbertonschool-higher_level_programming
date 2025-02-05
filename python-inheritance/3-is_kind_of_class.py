#!/usr/bin/python3
"""
Public instance return true if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class else return false
"""


def is_kind_of_class(obj, a_class):
    """
    Public instance return true if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class else return false
    """
    return isinstance(obj, a_class)
