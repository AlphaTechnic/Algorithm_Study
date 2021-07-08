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


def get_chicken_dist(selected_chickens):
    tot = 0

    for y_h, x_h in home_poses:
        min_val = 10 * 8
        for y_c, x_c in selected_chickens:
            min_val = min(min_val, abs(y_h - y_c) + abs(x_h - x_c))
        tot += min_val

    return tot


selected_chicken_list = list(combinations(chicken_poses, M))
ans = 10**8
for selected_chickens in selected_chicken_list:
    # M개 선택해서 그 매장만 부활
    for r, c in selected_chickens:
        board[r][c] = 2

    # 치킨 거리 구함
    tmp = get_chicken_dist(selected_chickens)
    ans = min(tmp, ans)

    # resotre
    for r, c in selected_chickens:
        board[r][c] = 0

print(ans)