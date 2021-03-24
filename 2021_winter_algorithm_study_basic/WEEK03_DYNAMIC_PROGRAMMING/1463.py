import sys
sys.stdin = open("input.txt", "r")

N = int(input())

dp = [0 for _ in range(N+1)]
for i in range(2, N+1):
    a = b = c = 1000000
    if i % 3 == 0:
        a = dp[int(i/3)] + 1
    if i % 2 == 0:
        b = dp[int(i/2)] + 1
    c = dp[i-1] + 1
    dp[i] = min(a, b, c)

print(dp[N])