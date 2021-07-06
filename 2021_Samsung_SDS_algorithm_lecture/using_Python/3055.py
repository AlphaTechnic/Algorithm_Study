"""
input :
3 3
D.*
...
.S.

output :
3
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

R, C = map(int, input().split())
BOARD = []
for _ in range(R):
    BOARD.append(list(input().rstrip()))

W_pos = []
for r in range(R):
    for c in range(C):
        if BOARD[r][c] == 'D':
            D_pos = [r, c]
        elif BOARD[r][c] == 'S':
            S_pos = [r, c]
        elif BOARD[r][c] == '*':
            W_pos.append([r, c])


move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs():
    w_visited = [[0 for _ in range(C)] for _ in range(R)]
    w_que = deque()
    for w_pos in W_pos:
        w_que.append(w_pos)
        w_visited[w_pos[0]][w_pos[1]] = 1

    s_visited = [[0 for _ in range(C)] for _ in range(R)]
    s_que = deque()
    s_que.append(S_pos)
    s_visited[S_pos[0]][S_pos[1]] = 1

    while True:
        loop_cnt = len(w_que)
        for _ in range(loop_cnt):
            cy, cx = w_que.popleft()
            for dy, dx in move:
                ny, nx = cy + dy, cx + dx

                if not (0 <= ny < R and 0 <= nx < C): continue
                if w_visited[ny][nx]: continue
                if BOARD[ny][nx] == 'D': continue
                if BOARD[ny][nx] == 'X': continue

                w_visited[ny][nx] = w_visited[cy][cx] + 1
                w_que.append([ny, nx])

        loop_cnt = len(s_que)
        for _ in range(loop_cnt):
            cy, cx = s_que.popleft()
            for dy, dx in move:
                ny, nx = cy + dy, cx + dx

                if not (0 <= ny < R and 0 <= nx < C): continue
                if s_visited[ny][nx]: continue
                if w_visited[ny][nx]: continue
                if BOARD[ny][nx] == 'X': continue

                s_visited[ny][nx] = s_visited[cy][cx] + 1
                if BOARD[ny][nx] == 'D':
                    print(s_visited[D_pos[0]][D_pos[1]] - 1)
                    return
                s_que.append([ny, nx])

        if len(s_que) == 0:
            print("KAKTUS")
            return


bfs()
