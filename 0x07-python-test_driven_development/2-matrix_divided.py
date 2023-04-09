#!/usr/bin/python3
"""

    Defines a function that divides all elements of a matrix

"""


def matrix_divided(matrix, div):

    """divides all elements of a matrix"""

    result = True
    size = len(matrix[0])
    length = True
    new_matrix = []

    for i in matrix:
        if len(i) != size:
            length = False
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                result = False

    if result is False:
        raise TypeError("matrix must be a matrix(list of lists)
                        of integers/floats")

    if length is False:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = list(map(lambda x: list(map(
        lambda y: round(y / div, 2), x)), matrix))
    return new_matrix
