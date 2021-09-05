"""
input :
9

output :
55
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 10007

if __name__ == "__main__":
    dp = [0 for _ in range(1001)]
    dp[1] = 1
    dp[2] = 2
    for i in range(3, 1001):
        dp[i] = (dp[i - 2] + dp[i - 1]) % MOD

    N = int(input())
    print(dp[N] % MOD)
