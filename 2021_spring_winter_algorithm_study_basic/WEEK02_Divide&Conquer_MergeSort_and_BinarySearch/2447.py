"""
input :
27
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = [['*' for _ in range(N)] for _ in range(N)]


def divide_and_conquer(start_r, start_c, size):
    if size == 1:
        return

    for r in range(start_r + size // 3, start_r + (size // 3) * 2):
        for c in range(start_c + size // 3, start_c + (size // 3) * 2):
            board[r][c] = ' '

    for r in range(start_r, start_r + size, size // 3):
        for c in range(start_c, start_c + size, size // 3):
            divide_and_conquer(r, c, size // 3)


divide_and_conquer(0, 0, N)
for r in range(N):
    for c in range(N):
        print(board[r][c], end='')
    print()
