#!/usr/bin/python3
"""

    Defines a function that adds two integers

"""


def add_integer(a, b=98):
    """
        Adds two integer
    s"""
    if not type(a) == int and not type(a) == float:
        raise TypeError("a must be an integer")
    if not type(b)== int and not type(b) == float:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
