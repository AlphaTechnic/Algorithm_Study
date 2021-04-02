"""
input :
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""

import sys

sys.setrecursionlimit(10000)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
ans = {'-1': 0, '0': 0, '1': 0}


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
        ans[str(board[start_r][start_c])] += 1
        return

    for r in range(start_r, start_r + size, size // 3):
        for c in range(start_c, start_c + size, size // 3):
            divide_and_conquer(r, c, size // 3)


divide_and_conquer(0, 0, N)

print(ans['-1'])
print(ans['0'])
print(ans['1'])
