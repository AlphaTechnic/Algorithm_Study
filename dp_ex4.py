"""
input :
2 15
2
3
"""

import sys
sys.stdin = open("input.txt", "r")

MAX = 10001

N, M = map(int, input().split())
units = []
for _ in range(N):
    units.append(int(input()))
units.sort()

dp = [MAX for _ in range(M+1)]

dp[0] = 0
for unit in units:
    for j in range(unit, M+1):
        dp[j] = min(dp[j], dp[j-unit] + 1) ##### critical point

if dp[M] == MAX:
    print(-1)
else:
    print(dp[M])
