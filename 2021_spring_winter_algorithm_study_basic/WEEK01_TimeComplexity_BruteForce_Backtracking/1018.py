"""
input :
10 13
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
BBBBBBBBWBWBW
BBBBBBBBBWBWB
WWWWWWWWWWBWB
WWWWWWWWWWBWB
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
board.append(['_'] * (C + 1))
for i in range(R):
    board.append(['_'] + list(input().rstrip()))

last_start_r = R - 7
last_start_c = C - 7

ans = 64
for start_r in range(1, last_start_r + 1):
    for start_c in range(1, last_start_c + 1):
        BWver = 0
        WBver = 0
        for r in range(start_r, start_r + 8):
            for c in range(start_c, start_c + 8):
                if (r + c) % 2 == 0:
                    if board[r][c] == 'B':
                        BWver += 1
                    elif board[r][c] == 'W':
                        WBver += 1
                elif (r + c) % 2 == 1:
                    if board[r][c] == 'W':
                        BWver += 1
                    elif board[r][c] == 'B':
                        WBver += 1
        ans = min(ans, min(BWver, WBver))

print(ans)
