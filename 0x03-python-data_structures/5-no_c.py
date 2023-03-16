#!/usr/bin/python3
def no_c(my_string):
    """
        remove all occurence of the 'c' and 'C' charcter from the string my_string without using replace()
    """
    
    new_str = ''
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string += ch

        return new_str
