"""
input :
18

output :
4
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N + 1)]

# edge case
if N == 3:
    print(1)
    exit()
if N == 4:
    print(-1)
    exit()

dp[3] = 1
dp[4] = 0
dp[5] = 1
for i in range(6, N + 1):
    if dp[i - 3] == 0 and dp[i - 5] == 0:  # 둘 다 0
        dp[i] = 0
    elif dp[i - 3] * dp[i - 5] == 0:  # 둘 중 하나만 0
        dp[i] = max(dp[i - 3], dp[i - 5]) + 1
    else:  # 둘 다 0 아님
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

if dp[N] == 0:
    print(-1)
else:
    print(dp[N])
