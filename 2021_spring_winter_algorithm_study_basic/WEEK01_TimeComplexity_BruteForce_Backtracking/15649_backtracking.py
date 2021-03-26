"""
input:
4 2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
ans = ['_' for _ in range(M + 1)]
isused = [False for _ in range(N + 1)]


def permute(lv):
    if lv == M:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return

    for i in range(1, N + 1):
        if isused[i] == False:
            isused[i] = True
            ans[lv] = i

            permute(lv + 1)

            isused[i] = False # 복원


permute(0)
