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
for i in range(R):
    board.append(list(map(int, input().split())))

print(board)