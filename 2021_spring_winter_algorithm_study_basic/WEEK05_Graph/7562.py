"""
input :
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1

output :
5
28
0
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

move = [[-2, 1], [-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1]]
def bfs(s_pos):
    que = deque()
    que.append(s_pos)
    board[s_pos[0]][s_pos[1]] = 1

    while len(que) != 0:
        cy, cx = que.popleft()
        if [cy, cx] == tar_pos:
            print(board[cy][cx] - 1)
            break

        for dy, dx in move:
            ny = cy + dy
            nx = cx + dx
            if not 0 <= ny < N: continue
            if not 0 <= nx < N: continue
            if board[ny][nx] != 0: continue

            board[ny][nx] = board[cy][cx] + 1
            que.append([ny, nx])


T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    start_pos = list(map(int, input().rstrip().split()))
    tar_pos = list(map(int, input().rstrip().split()))
    board = [[0 for _ in range(N)] for _ in range(N)]

    bfs(start_pos)
