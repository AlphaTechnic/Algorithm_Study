import sys
sys.stdin = open("input.txt", "r")

MOD = 1000000007
dp = [0 for _ in range(1516)]

N = int(input())

if N == 1:
    print(0)
else:
    dp[2] = 1
    dp[3] = 1
    for i in range(4, 1516):
        dp[i] = 2*dp[i-2] + dp[i-1]

    print(dp[N] % MOD)

