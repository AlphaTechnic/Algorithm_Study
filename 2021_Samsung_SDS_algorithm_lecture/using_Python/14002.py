"""
input :
6
10 20 10 30 20 50

output :
4
10 20 30 50
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    nums = [0] + list(map(int, input().rstrip().split()))

    # i번째 원소를 마지막 원소로 넣는 최장증가수열의 길이
    dp = [0 for _ in range(0, N + 1)]
    parent = [-1 for _ in range(0, N + 1)]
    for i in range(1, N + 1):
        max_dpval = 0
        max_dpind = -1
        for j in range(i):
            if dp[j] > max_dpval and nums[j] < nums[i]:
                max_dpval = dp[j]
                max_dpind = j
        dp[i] = max_dpval + 1
        parent[i] = max_dpind

    max_dpval = 0
    max_dpind = -1
    for i, dpval in enumerate(dp):
        if max_dpval < dp[i]:
            max_dpval = dpval
            max_dpind = i

    # 길이 print
    print(max_dpval)

    # 수열 print
    dq = deque()
    while max_dpind != -1:
        dq.appendleft(nums[max_dpind])
        max_dpind = parent[max_dpind]

    for num in dq:
        print(num, end=' ')
