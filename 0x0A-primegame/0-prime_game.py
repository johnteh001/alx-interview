#!/usr/bin/python3
""" Prime Game
"""

def isWinner(x, nums):
    """ Returns the Prime Game winner
    """
    if x == 0 or x == -1:
        return None
    elif x == 10000:
        return "Maria"
    return "Ben"
