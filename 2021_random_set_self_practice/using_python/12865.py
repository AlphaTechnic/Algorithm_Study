"""
input :
4 7
6 13
4 8
3 6
5 12

oupput :
14
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())

    V = []
    W = []
    for _ in range(N):
        w, v = map(int, input().rstrip().split())
        W.append(w)
        V.append(v)

    dp = [[0 for _ in range(K + 1)] for _ in range(N)]
    for i in range(N):
        for k in range(K + 1):
            if k - W[i] >= 0:
                dp[i][k] = max(dp[i - 1][k], dp[i - 1][k - W[i]] + V[i])
            else:
                dp[i][k] = dp[i - 1][k]
    print(dp[N - 1][K])
