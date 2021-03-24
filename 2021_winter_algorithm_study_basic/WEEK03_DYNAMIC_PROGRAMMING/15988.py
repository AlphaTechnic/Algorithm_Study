import sys
sys.stdin = open("input.txt", 'r')
MOD = 1000000009

dp = [-1 for _ in range(1000001)]


def num_of_split_by_1_2_3(n):
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, n+1):
        dp[i] = (dp[i - 3] + dp[i - 2] + dp[i - 1]) % MOD
    return dp[n]


T = int(input())
num_of_split_by_1_2_3(1000000)
for i in range(T):
    n = int(input())
    print(dp[n])
