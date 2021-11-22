"""
input :
5
A
BC
DEF
GHJI
KLONM

output :
35
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

toint = dict()
for i in range(65, 65 + 26):
    toint[chr(i)] = i - 64

if __name__ == "__main__":
    N = int(input())
    dp = [[0 for _ in range(N + 2)] for _ in range(N)]

    for i in range(N):
        ln = list(input().rstrip())
        for j in range(len(ln)):
            dp[i][j + 1] = toint[ln[j]]
    # print(dp)

    for i in range(1, len(dp)):
        for j in range(1, i + 2):
            # print(dp[i][j])
            dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])

    print(max(dp[-1]))
