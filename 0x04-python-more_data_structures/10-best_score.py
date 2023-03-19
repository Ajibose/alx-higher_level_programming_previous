#!/usr/bin/python3
def best_score(a_dictionary):
    """
        Returns a key with the biggest integer value.
    """

    if not a_dictionary:
        return None
    big_key = None
    big_val = 0

    for key, val in a_dictionary.items():
        if val > big_val:
            big_val = val
            big_key = key

    return big_key
