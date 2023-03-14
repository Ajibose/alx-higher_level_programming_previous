#!/usr/bin/python3
def element_at(my_list, idx):

    """
        Retrieve the element with index idx from the list my_list
    """

    length = len(my_list)
    if idx < 0 || idx > length - 1:
        return None

    return my_list[idx]
