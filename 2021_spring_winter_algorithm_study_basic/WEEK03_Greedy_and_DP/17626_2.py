"""
input :
11339

output :
3
"""

import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [4 for _ in range(N+1)]
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[i - j**2] + 1)

print(dp[N])