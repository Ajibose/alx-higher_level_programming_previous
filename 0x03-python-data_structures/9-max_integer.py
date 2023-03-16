#!/usr/bin/python3
def max_integer(my_list=[]):
    """
        finds the biggest integer of a list.
    """

    if len(my_list) == 0:
        return None

    max_val = my_list[0]
    for item in my_list:
        if item > max_val:
            max_val = item

    return max_val
