"""
input :
5 3 19

output :
10011
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, L, I = map(int, input().rstrip().split())

    dp = [[0 for _ in range(32)] for _ in range(32)]

    # dp[i][j] = (길이 i, 1의 개수 j) 인 prefix를 가진 이진수 개수
    for i in range(31):
        dp[0][i] = 1
    for i in range(1, 32):
        dp[i][0] = dp[i - 1][0]
        for j in range(1, 32):
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

    for n in range(N - 1, -1, -1):
        if I <= dp[n][L]:
            print('0', end="")
        else:
            print('1', end="")
            I -= dp[n][L]
            L -= 1
