#!/usr/bin/python3
def element_at(my_list, idx):

    """
        Retrieve the element with index idx from the list my_list
    """

    length = len(my_list)
    if idx < 0 || idx > length:
        return None

    for i in range(length):
        if idx == i:
            print("{}".format(my_list[i]))
            break
