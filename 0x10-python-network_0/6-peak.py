#!/usr/bin/python3

"""
Find Peak
"""

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers
    """
    if not list_of_integers:
        return None

    l = 0
    r = len(list_of_integers) - 1

    while l < r:
        mid = (l + r) // 2
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            l = mid + 1
        else:
            r = mid
    return list_of_integers[l]
