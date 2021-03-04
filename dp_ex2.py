"""
input :
4
1 3 1 5
"""

import sys

sys.stdin = open("input.txt", "r")

N = int(input())
data = [0] + list(map(int, input().split()))

# a_i = max(a_(i-1), a_(i-2) + k_i), a_0 = 0, a_1 = k_1
dp = [0 for _ in range(N + 1)]
dp[1] = data[1]
for i in range(2, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + data[i])

print(dp[N])
