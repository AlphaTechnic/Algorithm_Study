"""
input :
11
8 3 2 4 8 7 2 4 0 8 8

output :
10
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def recur(ind, tot):
    global K
    global cnt
    if ind == N - 1:
        if tot == K:
            return 1
        else:
            return 0
    if not 0 <= tot <= 20:
        return 0
    if dp[ind][tot]:
        return dp[ind][tot]

    a = recur(ind + 1, tot + nums[ind])
    b = recur(ind + 1, tot - nums[ind])
    dp[ind][tot] = a + b
    return dp[ind][tot]


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    K = nums[-1]
    nums.pop()

    # dp[(ind, tot)] : ind가 처리되었을 때(뒤의 ind 부터 처리해 감), 합이 tot인 경우의 수`
    dp = [[0 for _ in range(21)] for _ in range(101)]
    print(recur(1, nums[0]))
