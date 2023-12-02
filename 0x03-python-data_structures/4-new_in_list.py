#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copied_list = my_list[:]
    if idx < 0:
        return copied_list
    elif idx > len(my_list):
        return copied_list
    else:
        copied_list[idx] = element
        return copied_list
