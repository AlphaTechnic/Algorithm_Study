"""
연구소
input :
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""

import sys
import itertools

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def restore():
    for r in range(R):
        for c in range(C):
            board[r][c] = board_origin[r][c]


def spread_by_dfs(y, x):
    st = []
    st.append((y, x))
    while st:
        cy, cx = st.pop()
        for dy, dx in move:
            ny, nx = cy + dy, cx + dx
            if not 0 <= ny < R: continue
            if not 0 <= nx < C: continue
            if board[ny][nx] == 0:
                board[ny][nx] = 2  # 바이러스를 퍼지게 함
                st.append((ny, nx))


def get_score():
    cnt = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                cnt += 1
    return cnt


R, C = map(int, input().split())
board = [[0 for _ in range(C)] for _ in range(R)]
board_origin = []
for _ in range(R):
    board_origin.append(list(map(int, input().split())))
restore()

move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
pos_0 = []  # 안전지
pos_2 = []  # 바이러스
for r in range(R):
    for c in range(C):
        if board[r][c] == 0:
            pos_0.append((r, c))
        elif board[r][c] == 2:
            pos_2.append((r, c))

combi_3 = list(itertools.combinations(pos_0, 3))

max_val = 0
for combi in combi_3:
    for y, x in combi:
        board[y][x] = 1
    for vy, vx in pos_2:  # virus_y, virus_x
        spread_by_dfs(vy, vx)
    tmp_val = get_score()
    if tmp_val > max_val:
        max_val = tmp_val
    restore()

print(max_val)
