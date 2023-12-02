#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for idx, column in enumerate(row):
            if idx == len(row) - 1:
                print("{:d}".format(column), end="")
            else:
                print("{:d} ".format(column), end="")
        print()
