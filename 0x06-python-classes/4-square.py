#!/usr/bin/python3
"""
    A module that defines a class square based on 3-main.py
"""


class Square():
    """
    A class that defines a square
    """
    def __init__(self, size=0):
        """
            Initializes a square

            Args:
                size(int): The length of the square
        """
        self.__size = size

    def area(self):
        """Computes the area of a square

            Returns:
                int: Area of square
        """
        return self.__size * self.__size

    @property
    def size(self):
        """Retrieve te size of the square

           Returns:
           int: The square size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
            Gets the square size
        """
        if type(value) == int:
            if (value > 0):
                self.__size = value
            else:
                raise ValueError("Size must be >= :0")
        else:
            raise TypeError("Size must be an integer")
