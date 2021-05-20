"""
input :
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10

output :
3
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, L, R = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def bfs(S):
    union_mems = set()

    que = deque()
    que.append((S[0], S[1]))
    visited[S[0]][S[1]] = True
    union_mems.add((S[0], S[1]))

    while len(que) != 0:
        cy, cx = que.popleft()
        if not visited[cy][cx]:
            visited[cy][cx] = True

        for dy, dx in move:
            ny, nx = cy + dy, cx + dx

            if not 0 <= ny < N: continue
            if not 0 <= nx < N: continue
            if visited[ny][nx]: continue

            if L <= abs(board[cy][cx] - board[ny][nx]) <= R:
                que.append((ny, nx))
                union_mems.add((ny, nx))
                visited[ny][nx] = True

    if len(union_mems) > 1:
        unions.append(union_mems)

cnt = 0
while True:
    unions = []
    visited = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                bfs([r, c])

    for SET in unions:
        tot = 0
        for pos in SET:
            tot += board[pos[0]][pos[1]]
        for pos in SET:
            board[pos[0]][pos[1]] = tot // len(SET)

    if len(unions) != 0:
        cnt += 1
    else:
        break

print(cnt)