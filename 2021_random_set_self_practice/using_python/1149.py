"""
input :
3
26 40 83
49 60 57
13 89 99

output :
96
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[0, 0, 0]] + [list(map(int, input().rstrip().split())) for _ in range(N)]

    for i in range(2, N + 1):
        for clr in range(3):
            if clr == 0:
                dp[i][clr] = dp[i][clr] + min(dp[i - 1][1], dp[i - 1][2])
            elif clr == 1:
                dp[i][clr] = dp[i][clr] + min(dp[i - 1][0], dp[i - 1][2])
            elif clr == 2:
                dp[i][clr] = dp[i][clr] + min(dp[i - 1][0], dp[i - 1][1])

    print(min(dp[N]))
