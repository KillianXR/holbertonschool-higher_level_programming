#!/usr/bin/python3
"""function that return the len of a folder"""


def append_write(filename="", text=""):
    """function that return the len of a folder"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
