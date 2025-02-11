#!/usr/bin/python3
"""function that return the JSON representation of an object(string)"""
import json

def to_json_string(my_obj):
    """function that return the JSON representation of an object"""
    my_obj = json.dumps(my_obj)
    return my_obj