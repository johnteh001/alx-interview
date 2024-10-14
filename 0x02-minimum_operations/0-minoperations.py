#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Function determines min operations of two functions on a file"""
    min_ops = 0
    if n <= 1:
        return min_ops
    for i in range(2, n + 1):
        while (n % i == 0):
            min_ops = min_ops + i
            n = n / i
            if n < i:
                break
    return min_ops
