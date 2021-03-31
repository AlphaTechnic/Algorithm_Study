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
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
ans = {'-1' : 0, '0' : 0, '1': 0}
print(board)

def divide_and_conquer(lv):
    size = N // lv

    for r_start in range(0, N, size):
        for c_start in range(0, N, size):
            for r in range(size):
                for c in range(size):
                    if board[r][c]