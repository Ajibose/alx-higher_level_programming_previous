#!/usr/bin/python3
"""
    Defines a function that encodes a python object and writes it to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Encodes an object and write it to a file

    Args:
        my_obj (obj): Object to encode
        filename (file): Path to file to write encoded string to

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
