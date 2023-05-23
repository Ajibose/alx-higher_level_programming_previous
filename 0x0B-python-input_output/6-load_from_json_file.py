#!/usr/bin/python3
"""
    Decodes a json string read from a file
"""
import json


def load_from_json_file(filename):
    """
    Decode a json string read from filename

    Args:
        filename (file): Path to file to get json string
    """
    with open(filename, encoding="utf-8") as f:
        json_str = f.read()
        obj = json.loads(json_str)
        return obj
