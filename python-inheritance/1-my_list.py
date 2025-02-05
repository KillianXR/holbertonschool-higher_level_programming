#!/usr/bin/python3
"""
Class of list.
"""


class MyList(list):

    def print_sorted(self):
        """public instance, that prints the list, but sorted."""
        print(sorted(self))
