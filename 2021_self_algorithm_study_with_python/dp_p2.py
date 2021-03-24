"""
정수 삼각형
input :
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = []
for i in range(N):
    dp.append(list(map(int, input().split())))

for r in range(1, N):
    dp[r][0] = dp[r-1][0]+dp[r][0]
    dp[r][r] = dp[r-1][r-1]+dp[r][r]
    for c in range(1, r-1):
        dp[r][c] = max(dp[r-1][c-1], dp[r-1][c]) + dp[r][c]

print(max(dp[N-1]))