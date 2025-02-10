#!/usr/bin/python3
def write_file(filename="", text=""):
    """function that print the number of char of a folder"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return len(text)
