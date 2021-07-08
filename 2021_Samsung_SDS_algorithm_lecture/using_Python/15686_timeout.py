"""
input :
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

output :
10
"""

import sys
from itertools import combinations
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip().split())))

chicken_poses = []
home_poses = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            home_poses.append([r, c])
        elif board[r][c] == 2:
            chicken_poses.append([r, c])

# 치킨집 다 폐업시킴
for r, c in chicken_poses:
    board[r][c] = 0



move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
def bfs(r, c, chk_board):
    chk_board = [[-1 for _ in range(N)] for _ in range(N)]
    que = deque()
    que.append([r, c])
    chk_board[r][c] = 0

    while len(que) != 0:
        cy, cx = que.popleft()

        for dy, dx in move:
            ny, nx = cy + dy, cx + dx

            if not 0 <= ny < N: continue
            if not 0 <= nx < N: continue
            if chk_board[ny][nx] != -1: continue

            chk_board[ny][nx] = chk_board[cy][cx] + 1
            if board[ny][nx] == 2:
                return chk_board[ny][nx]

            que.append([ny, nx])

    return 0


def get_chicken_dist():
    tot = 0
    for r, c in home_poses:
        chk_board = list()
        min_dist = bfs(r, c, chk_board)
        tot += min_dist
    return tot


selected_chicken_list = list(combinations(chicken_poses, M))
ans = 10**8
for selected_chickens in selected_chicken_list:
    # M개 선택해서 그 매장만 부활
    for r, c in selected_chickens:
        board[r][c] = 2

    # 치킨 거리 구함
    tmp = get_chicken_dist()
    ans = min(tmp, ans)

    # resotre
    for r, c in selected_chickens:
        board[r][c] = 0

print(ans)