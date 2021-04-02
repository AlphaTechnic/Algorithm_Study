"""
input:
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

output :
((110(0101))(0010)1(0001))
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, list(input().rstrip()))))


def divide_and_conquer(start_r, start_c, size):
    escape_flag = 0
    for r in range(start_r, start_r + size):
        for c in range(start_c, start_c + size):
            if board[r][c] != board[start_r][start_c]:
                escape_flag = 1
                break
        if escape_flag == 1:
            break
    if escape_flag == 0:
        print(board[start_r][start_c], end='')
        return

    print('(', end='')
    for r in range(start_r, start_r + size, size // 2):
        for c in range(start_c, start_c + size, size // 2):
            divide_and_conquer(r, c, size // 2)
    print(')', end='')


divide_and_conquer(0, 0, N)
