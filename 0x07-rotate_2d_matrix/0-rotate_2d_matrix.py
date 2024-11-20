#!/usr/bin/python3
"""Rotate 2D matrix
"""


def rotate_2d_matrix(matrix):
    """Rotates the matrix 90 degrees clockwise
    """
    temp = matrix
    le = len(temp)
    main = []
    for i in range(le):
        lis = []
        for j in range(1, le + 1):
            lis.append(temp[le - j][i])
        main.append(lis)
    for i in range(le):
        for j in range(le):
            matrix[i][j] = main[i][j]
