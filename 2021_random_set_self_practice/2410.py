"""
input :
7

output :
6
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 1000000000

if __name__ == "__main__":
    dp = [0 for _ in range(1000001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 1000001):
        if i & 1 == 1:
            dp[i] = dp[i - 1]
        else:
            dp[i] = (dp[i - 1] + dp[i // 2]) % MOD

    N = int(input())
    print(dp[N])
