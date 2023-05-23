#!/usr/bin/python3
""""
    Define a function that appends to a file
"""
def append_write(filename="", text=""):
    """"
    Append to text t filename

    Args:
        filename (file): The path to the file to append to
        text (str): the string to append to filename

    """
    with open(filename, 'a', encoding="utf-8") as f:
        chs = f.write(text)
        return chs
