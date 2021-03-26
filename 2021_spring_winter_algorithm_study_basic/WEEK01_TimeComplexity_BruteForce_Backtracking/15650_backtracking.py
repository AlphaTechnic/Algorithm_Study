"""
input:
4 2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [i for i in range(N + 1)]
ans = []


def combi(lv, num):
    if lv == M + 1:
        for i in range(M):
            print(ans[i], end=' ')
        print()
        return

    for i in range(num, N + 1):  # lv 부터 참조, 마지막 숫자보다 커야함
        ans.append(num_list[i])

        combi(lv + 1, i + 1)

        ans.pop()


combi(1, 1)
