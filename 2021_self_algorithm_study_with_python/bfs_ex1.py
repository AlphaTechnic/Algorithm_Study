"""
input :
5 6
101010
111111
000001
111111
111111
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")

moves = [(1, 0), (0, 1), (-1, 0), (0, 1)] # r, d, l, u


def bfs():
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            if not 0 <= nx < C:
                continue
            if not 0 <= ny < R:
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = board[cy][cx] + 1
                queue.append((nx, ny))
    return board[ny-1][nx-1]


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input())))

queue = deque([(0, 0)])
print(bfs())
