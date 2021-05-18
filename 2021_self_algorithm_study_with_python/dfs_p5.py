"""
input :
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

output :
YES
"""

import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input().rstrip())
board = []
for _ in range(N):
    board.append(input().rstrip().split())

pos_T = []
pos_X = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            pos_T.append([i, j])
        elif board[i][j] == 'X':
            pos_X.append([i, j])


def is_success():
    barriers = list(combinations(pos_X, 3))
    for bar1, bar2, bar3 in barriers:
        #  reset
        board[bar1[0]][bar1[1]] = 'B'
        board[bar2[0]][bar2[1]] = 'B'
        board[bar3[0]][bar3[1]] = 'B'

        for r, c in pos_T:
            if not dfs([r, c]):
                # restore
                board[bar1[0]][bar1[1]] = 'X'
                board[bar2[0]][bar2[1]] = 'X'
                board[bar3[0]][bar3[1]] = 'X'
                break
        else:
            return True

    return False


move = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 우, 하, 좌, 상
def dfs(start):
    cy, cx = start[0], start[1]

    for dy, dx in move:
        ny, nx = cy, cx
        while True:
            ny, nx = ny + dy, nx + dx
            if not 0 <= ny < N: break
            if not 0 <= nx < N: break
            if board[ny][nx] == 'B': break
            if board[ny][nx] == 'S': return False

    return True


if is_success():
    print('YES')
else:
    print("NO")
