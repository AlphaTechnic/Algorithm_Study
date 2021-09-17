"""
input :
3
4
7
10

output :
7
44
274
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    dp = [0 for _ in range(12)]
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    for i in range(4, 12):
        dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(dp[N])
