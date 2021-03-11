"""
경쟁적 전염
input :
3 3
1 0 2
0 0 0
3 0 0
2 3 2
"""

import sys
import collections as col

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    q = col.deque()
    for type, y, x in pos:
        q.append((type, 0, y, x))

    while q:
        type, time, cy, cx = q.popleft()
        if time == S:
            return

        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not 1 <= ny < N + 1: continue
            if not 1 <= nx < N + 1: continue
            if board[ny][nx] != 0: continue

            board[ny][nx] = type
            q.append((type, time + 1, ny, nx))
    return


N, K = map(int, input().split())
board = [[0 for _ in range(N + 1)]]
for _ in range(N):
    board.append([0] + list(map(int, input().split())))
S, Y, X = map(int, input().split())

pos = []
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if board[r][c] != 0:
            pos.append((board[r][c], r, c))
pos.sort()

bfs()

# for r in range(1, N + 1):
#     for c in range(1, N + 1):
#         print(board[r][c], end=' ')
#     print()
print(board[Y][X])
