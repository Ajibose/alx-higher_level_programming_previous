#!/usr/bin/python3
"""
    Define a that reads a text file and prints its output to standard output
"""


def read_file(filename=""):
    """
    Reads filename and output its contenet to stdout

    Args:
        filename (str): path to the file to read

    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
