#!/usr/bin/python3
"""
    Defines a function that writs to a file
"""


def write_file(filename="", text=""):
    """
    Writes to filename

    Args:
        filename (str): path to the file to write
        text (str): character to write to filename

    """
    with open(filename, 'w', encoding="utf-8") as f:
        byte = f.write(text)
        return byte
