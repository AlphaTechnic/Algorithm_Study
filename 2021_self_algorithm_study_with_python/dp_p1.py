"""
금광
input :
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    arr = list(map(int, input().split()))
    dp = []
    for i in range(0, len(arr), C):
        dp.append(arr[i:i + C])

    for c in range(1, C):
        dp[0][c] = max(dp[0][c - 1], dp[1][c - 1]) + dp[0][c]
        dp[R - 1][c] = max(dp[R - 1][c - 1], dp[R - 2][c - 1]) + dp[R - 1][c]
        for r in range(1, R - 1):
            dp[r][c] = max(dp[r - 1][c - 1], dp[r][c - 1], dp[r + 1][c - 1]) + dp[r][c]

    max_val = 0
    for r in range(R):
        if dp[r][C - 1] > max_val:
            max_val = dp[r][C - 1]
    print(max_val)
