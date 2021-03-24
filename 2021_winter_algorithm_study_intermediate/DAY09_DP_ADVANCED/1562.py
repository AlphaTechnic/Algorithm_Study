import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

dp = [[[0 for _ in range(1<<10)] for _ in range(10)] for _ in range(101)]
mod = 1e9

N = int(input())
for i in range(1, 10):
    dp[1][i][1<<i] = 1

for i in range(1, N):
    for j in range(10):
        for k in range(1<<10):
            if dp[i][j][k] == 0:
                continue
            if (k & (1<<j)) == 0:
                continue
            if j+1 < 10:
                dp[i + 1][j + 1][k | 1 << (j+1)] += dp[i][j][k]
                dp[i + 1][j + 1][k | 1 << (j+1)] %= mod

            if j - 1 >= 0:
                dp[i + 1][j - 1][k | 1 << (j - 1)] += dp[i][j][k]
                dp[i + 1][j - 1][k | 1 << (j - 1)] %= mod

ans = 0
for i in range(10):
    ans += dp[N][i][(1 << 10) - 1]
    ans %= mod
print(int(ans))