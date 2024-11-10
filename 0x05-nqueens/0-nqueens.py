#!/usr/bin/python3
"""nqueens"""

import sys


def check_valid(board, row, col):
    """Determines the validy of queen position"""
    if 1 in board[row]:
        return False
    diag_up = zip(range(row, -1, -1), range(col, -1, -1))
    for i, j in diag_up:
        if board[i][j] == 1:
            return False
    diag_down = zip(range(row, len(board), 1), range(col, -1, -1))
    for i, j in diag_down:
        if board[i][j] == 1:
            return False
    return True


def helper_func(bord, column):
    """NQuuen helper function"""
    if column >= len(bord):
        display_board(bord, len(bord))
    for i in range(len(bord)):
        if check_valid(bord, i, column):
            bord[i][column] = 1
            res = helper_func(bord, column + 1)
            if res:
                return True
            bord[i][column] = 0
    return False


def display_board(board, n):
    """Prints board"""
    disp = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                disp.append([i, j])
    print(disp)


def main():
    """nqueens"""
    if not len(sys.argv) == 2:
        print("Usage: nqueens N")
        sys.exit(1)
    N = sys.argv[1]
    if not N.isnumeric():
        print("N must be a number")
        sys.exit(1)
    if int(N) < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = []
    for n in range(int(N)):
        row = [0] * int(N)
        board.append(row)
    helper_func(board, 0)


if __name__ == "__main__":
    main()
