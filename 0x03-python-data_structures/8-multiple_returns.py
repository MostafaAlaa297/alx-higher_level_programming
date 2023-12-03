#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    else:
        a = tuple(sentence)
        first = a[0]
        length = len(a)
        return length, first

