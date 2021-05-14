"""
input :
6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1

output :
6
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

C, R = map(int, input().rstrip().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().rstrip().split())))
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(pos1_list):
    que = deque()
    for pos1 in pos1_list:
        que.append(pos1)

    while len(que) != 0:
        cy, cx = que.popleft()
        for dy, dx in move:
            ny = cy + dy
            nx = cx + dx

            if not 0 <= ny < R: continue
            if not 0 <= nx < C: continue
            if board[ny][nx] != 0: continue

            board[ny][nx] = board[cy][cx] + 1
            que.append([ny, nx])


pos1s = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 1:
            pos1s.append([r, c])

bfs(pos1s)

max_val = -1
for r in range(R):
    for c in range(C):
        max_val = max(max_val, board[r][c])
        if board[r][c] == 0:
            print(-1)
            exit()
else:
    print(max_val - 1)
