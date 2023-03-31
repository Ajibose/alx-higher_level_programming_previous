#!/usr/bin/python3
"""
    A module that defines a class square
"""


class Square():
    """
    A class that defines a square
    """
    def __init__(self, size=0):
        """
            Initializes a square
        """
        if type(size) == int:
            if (size > 0):
                self.__size = size
            else:
                raise ValueError("Size must greater or equal 0")
        else:
            raise TypeError("Size must be int")
