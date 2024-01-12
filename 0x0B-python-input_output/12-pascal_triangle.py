#!/usr/bin/python3
"""
================
pascal triangle
===============
"""

def pascal_triangle(n):
    """
    create pascal's triangle
    """
    if n <= 0:
        return []
    
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        print("row: {}".format(row))
        print("i: {}".format(i))

        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
                print("j: {}".format(j))
                print("triangle[{} - 1][{} - 1]: {}".format(i, j, triangle[i-1][j-1]))
                print("triangle[{} - 1][{}]: {}".format(i, j, triangle[i-1][j]))
                print("triangle[i-1][j-1] + triangle[i-1][j]: {}".format(triangle[i-1][j-1] + triangle[i-1][j]))
        triangle.append(row)
        print("traingle: {}".format(triangle))

    return triangle
