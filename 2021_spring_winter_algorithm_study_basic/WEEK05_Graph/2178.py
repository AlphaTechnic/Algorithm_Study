"""
input :
4 6
101111
101010
101011
111011

output :
15
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().rstrip())))

visited = [[0 for _ in range(C)] for _ in range(R)]
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(s_pos):
    que = deque()
    que.append(s_pos)
    visited[s_pos[0]][s_pos[1]] = 1

    while len(que) != 0:
        cy, cx = que.popleft()

        for dy, dx in move:
            nx = cx + dx
            ny = cy + dy
            if not 0 <= nx < C: continue
            if not 0 <= ny < R: continue
            if not board[ny][nx]: continue
            if visited[ny][nx]: continue

            que.append([ny, nx])
            visited[ny][nx] += visited[cy][cx] + 1


bfs([0, 0])
print(visited[R - 1][C - 1])
