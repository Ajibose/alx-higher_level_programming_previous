#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
        Add the elements of the same index together in tuple_a andtuple_b
            and returns a tuple to those additions
    """

    tuple_c = ()

    if len(tuple_a) < 2:
        for i in range(2 - len(tuple_a)):
            tuple_a = tuple_a + (0, )

    if len(tuple_b) < 2:
        for i in range(2 - len(tuple_b)):
            tuple_b = tuple_b + (0, )

    tuple_c = tuple_c + (tuple_a[0] + tuple_b[0],)
    tuple_c = tuple_c + (tuple_a[1] + tuple_b[1],)

    return tuple_c
