"""
input :
8
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
column_used = [False for _ in range(N + 1)]
right_diagonal_used = [False for _ in range(2*N)]
left_diagonal_used = [False for _ in range(2*N+1)]

cnt = 0
def n_queen(lv):
    global cnt
    if lv == N+1: # 탈출 조건
        cnt += 1
        return
    for c in range(1, N+1):
        right_diagonal = (N - 1) + (c - lv)
        left_diagonal = c+lv

        if column_used[c]: continue
        if right_diagonal_used[right_diagonal]: continue
        if left_diagonal_used[left_diagonal]: continue

        column_used[c] = True
        right_diagonal_used[right_diagonal] = True
        left_diagonal_used[left_diagonal] = True

        n_queen(lv+1)

        # 복원
        column_used[c] = False
        right_diagonal_used[right_diagonal] = False
        left_diagonal_used[left_diagonal] = False

n_queen(1)
print(cnt)