#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
        Add the elements of the same index together in tuple_a andtuple_b
            and returns a tuple to those additions
    """

    tuple_c = ()

    if len(tuple_a) < len(tuple_b):
        for i  in range(len(tuple_b) - len(tuple_a)):
            tuple_a = tuple_a + (0,)
    elif len(tuple_b) < len(tuple_a):
        for i  in range(len(tuple_a) - len(tuple_b)):
            tuple_b = tuple_b + (0,)

    for i in range(len(tuple_a)):
        for j in range(len(tuple_b)):
            if j == i:
                add = tuple_a[i] + tuple_b[j]
                tuple_c = tuple_c + (add,)
                break

    return tuple_c
