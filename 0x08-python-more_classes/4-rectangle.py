#!/usr/bin/python3
"""
    Defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """A class tha defines a rectangle obect

    Attributes:
        width(int): width of the rectangle
        height(int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rec_list = []
        for i in range(self.__height):
            rec_list.append([])
            for j in range(self.__width):
                rec_list[i].append("#")
        my_rec = "\n".join([''.join(map(str, sublist))
                            for sublist in rec_list])
        return my_rec

    def __repr__(self):
        return "{}({}, {})".format(
                type(self).__name__, self.__width, self.__height)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__height + self.__width)
