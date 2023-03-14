#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
        Replaces an elent in the idx position in my_list list
    """

    length = len(my_list)
    if idx < 0 or idx > length - 1:
        return my_list

    my_list[idx] = element
    return my_list
