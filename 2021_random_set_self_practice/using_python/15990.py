"""
input :
3
4
7
10

output :
3
9
27
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MOD = 1000000009

if __name__ == "__main__":
    dp = [[0 for _ in range(4)] for _ in range(11)]
    dp[1][1] = 1; dp[1][2] = 0; dp[1][3] = 0;
    dp[2][1] = 0; dp[2][2] = 1; dp[2][3] = 0;
    dp[3][1] = 1; dp[3][2] = 1; dp[3][3] = 1;
    for i in range(4, 11):
        dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % MOD
        dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % MOD
        dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % MOD

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(sum(dp[N]) % MOD)
