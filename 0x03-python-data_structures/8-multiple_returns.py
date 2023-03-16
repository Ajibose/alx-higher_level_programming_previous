#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if not sentence:
        first = None
    else:
        first = sentence[0]

    tuple_sen = (length, first)
    return tuple_sen
