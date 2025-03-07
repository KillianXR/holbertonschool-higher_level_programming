#!/usr/bin/python3
"""
function that writes an Object to a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    function that writes an Object to a text file, using a JSON representation
    """
    with open(filename, 'w', encoding="utf-8") as f:
        my_obj = json.dumps(my_obj)
        f.write(my_obj)
