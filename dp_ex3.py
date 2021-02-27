import sys
sys.stdin = open("input.txt", "r")

N = int(input())

# a_i = a_(i-1) + 2*a_(i-2)
dp = [0 for _ in range(N+1)]
dp[1] = 1
dp[2] = 3
for i in range(3, N+1):
    dp[i] = dp[i-1] + 2*dp[i-2]

print(dp[N])