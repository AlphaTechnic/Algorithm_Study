"""
input :
8
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
col = [-1 for _ in range(N + 1)]


def promising(ind):
    for pre in range(ind):
        if col[pre] == col[ind] or abs(col[pre] - col[ind]) == ind-pre:
            return False
    return True


cnt = 0
def n_queen(i):
    global cnt
    if i == N:
        cnt += 1
    else:
        for row in range(N):
            col[i] = row
            if promising(i):
                n_queen(i + 1)

n_queen(0)
print(cnt)