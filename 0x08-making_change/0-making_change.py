#!/usr/bin/python3
"""Making Change
"""


def makeChange(coins, total):
    """Function returns fewest number of coins to make total
    """
    if total < 0:
        return 0
    temp = 0
    coins.sort(reverse=True)

    for coin in coins:
        if total % coin <= total:
            temp += total // coin
            total = total % coin
    return (temp if (total == 0) else -1)
