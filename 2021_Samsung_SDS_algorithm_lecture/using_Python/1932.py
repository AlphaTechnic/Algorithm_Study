"""
input :
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

output :
30
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    nums = list(map(int, input().rstrip().split()))
    for j, num in enumerate(nums):
        dp[i][j] = num

for i in range(1, N):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] += dp[i - 1][j]
        elif j == i:
            dp[i][j] += dp[i - 1][j - 1]
        else:
            dp[i][j] = max(dp[i - 1][j - 1] + dp[i][j], dp[i - 1][j] + dp[i][j])

print(max(dp[-1]))
