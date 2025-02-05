#!/usr/bin/python3
"""
returns the list of available attributes and methods of an object passed in
"""

def lookup(obj):
			"""returns the list of available attributes and methods of an object"""
			return dir(obj)
