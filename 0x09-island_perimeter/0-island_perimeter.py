#!/usr/bin/python3
"""Island Perimeter
"""


def island_perimeter(grid):
    """Function determines and returns the perimeter of Island
    """
    m = len(grid)
    n = len(grid[0])
    land, border = 0, 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                land += 1
                if ((i < m - 1) and (grid[i + 1][j] == 1)):
                    border += 1
                if ((j < n - 1) and (grid[i][j+1] == 1)):
                    border += 1
    perimeter = land * 4 - border * 2
    return perimeter
