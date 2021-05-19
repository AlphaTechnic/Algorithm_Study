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
solved = [[False for _ in range(N)] for _ in range(N)]
action_flag = False


def union_by_bfs(S):
    global action_flag
    union_members = set()

    que = deque()
    que.append([S[0], S[1]])
    union_members.add((S[0], S[1]))
    visited[S[0]][S[1]] = True
    solved[S[0]][S[1]] = True

    while len(que) != 0:
        cy, cx = que.popleft()
        if not visited[cy][cx]: visited[cy][cx] = True

        for dy, dx in move:
            ny, nx = cy + dy, cx + dx

            if not 0 <= ny < N: continue
            if not 0 <= nx < N: continue
            if visited[ny][nx]: continue

            if L <= abs(board[cy][cx] - board[ny][nx]) <= R:
                que.append([ny, nx])
                if (ny, nx) not in union_members:
                    union_members.add((ny, nx))


    if len(union_members) != 1:
        for set_to_change in sets_to_change:
            for y, x in union_members:
                if (y, x) in set_to_change:
                    return
        else:
            for y, x in union_members:
                solved[y][x] = True
            sets_to_change.append(union_members)


num_of_mov = 0
while True:
    sets_to_change = []
    solved = [[False for _ in range(N)] for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if not solved[r][c]:
                visited = [[False for _ in range(N)] for _ in range(N)]
                union_by_bfs([r, c])

    if len(sets_to_change) != 0:
        for union_mems in sets_to_change:

            tot = 0
            for y, x in union_mems:
                tot += board[y][x]
            new_val = tot // len(union_mems)

            for y, x in union_mems:
                board[y][x] = new_val
        num_of_mov += 1
    else:
        break

print(num_of_mov)