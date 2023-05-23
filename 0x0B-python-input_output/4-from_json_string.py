#!/usr/bin/python3
"""
    Defines a function that decodes a json string
"""
import json


def from_json_string(my_str):
    """
    Coverts an encoded json_string back to python object

    Args:
        my_str (json str): The string to decode

    Returns:
        (obj): decoded python object
    """
    obj = json.loads(my_str)
    return obj
