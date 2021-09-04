"""
input :
3
4
7
10

output :
4
8
14
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    dp = [[0 for _ in range(4)] for _ in range(10001)]
    dp[0][1] = 1  # dp가 잘 정의되게 하기 위한 base case 정의
    dp[1][1] = 1
    dp[2][1] = 1
    dp[2][2] = 1
    for i in range(3, 10001):
        dp[i][1] = 1
        dp[i][2] = dp[i - 2][1] + dp[i - 2][2]
        dp[i][3] = dp[i - 3][1] + dp[i - 3][2] + dp[i - 3][3]

    T = int(input())
    for _ in range(T):
        N = int(input())
        print(sum(dp[N]))
