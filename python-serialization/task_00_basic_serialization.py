#!/usr/bin/env python3
import json
"""
module python that srialize and deserialize the content of a file
"""


def serialize_and_save_to_file(data, filename):
    """function that serialize and save content of a file"""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """function that load and deserialize content of a file"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
