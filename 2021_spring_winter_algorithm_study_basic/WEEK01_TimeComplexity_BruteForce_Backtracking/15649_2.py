"""
input:
4 2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
nums = ['_' for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]


def permute(cnt):
    if cnt == M:
        for i in range(M):
            print(nums[i], end=' ')
        print()

    for i in range(1, N + 1):
        if visited[i] == False:
            visited[i] = True
            nums[cnt] = i
            permute(cnt + 1)
            visited[i] = False


permute(0)
