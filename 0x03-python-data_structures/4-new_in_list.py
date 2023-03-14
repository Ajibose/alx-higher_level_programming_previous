#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
        Replaces the element at idx index of a shallow copy of my_list
    """

    if not my_list:
        return None

    if idx < 0 or idx > len(my_list) - 1:
        return my_list

    new_list = my_list[:]
    new_list[idx] = element
    return new_list
