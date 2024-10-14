#!/usr/bin/python3
"""
Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Returns
    list: integers representing Pascal's triangle
    """
    b_list = []
    if n <= 0:
        return b_list
    for i in range(1, n + 1):
        s_list = []
        m = 1
        for j in range(1, i + 1):
            s_list.append(m)
            m = int(m * (i - j) / j)
        b_list.append(s_list)
    return (b_list)
