"""
input :
6
10
20
15
25
10
20

output :
75
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    arr = [0]
    for _ in range(N):
        arr.append(int(input()))

    # dp[i][0] = i번째 계단을 1점프로 왔을 때, 최대점수
    # dp[i][1] = i번째 계단을 2점프로 왔을 때, 최대점수
    dp = [[0, 0] for _ in range(N + 1)]
    dp[1][0] = dp[1][1] = arr[1]
    for i in range(2, N + 1):
        dp[i][0] = dp[i - 1][1] + arr[i]
        dp[i][1] = max(dp[i - 2][0], dp[i - 2][1]) + arr[i]

    print(max(dp[-1]))