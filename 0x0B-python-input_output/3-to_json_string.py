#!/usr/bin/python3
"""
    Defines a function that encodes a python object to json string
"""
import json


def to_json_string(my_obj):
    """
    Convert an object to json

    Args:
        my_obj (object): Object to encode

    Returns:
        (str): The ecoded json string
    """
    json_str = json.dumps(my_obj)
    return json_str
