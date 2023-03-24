#!/usr/bin/python3
def weight_average(my_list=[]):
    """
        Calculated the weighrted average of a list of tuple
    """

    if my_list is None or len(my_list) < 1:
        return 0

    add, total, average, denom = 0, 0, 0, 0
    for i, j in my_list:
        add = i * j
        total += add
        denom += j

    average = total / denom
    return average
