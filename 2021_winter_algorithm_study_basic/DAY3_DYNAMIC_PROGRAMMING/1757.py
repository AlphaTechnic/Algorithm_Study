import sys
sys.stdin = open("input.txt", "r")

input_str = sys.stdin.readline()
N, M = map(int, input_str.split())
dp = [[[0, 0] for _ in range(M+5)] for _ in range(N+5)]

D = [0]*10001
for i in range(1, N+1):
    D[i] = int(input())

for i in range(1, N+1):
    for j in range(M+1):

        if j != 1:
            if j >= 2:
                # 달리다가 -> 달림
                dp[i][j][1] = dp[i-1][j-1][1] + D[i]
                # 달리다가 -> 쉼, 쉬다가 -> 쉼
                dp[i][j][0] = max(dp[i-1][j+1][1], dp[i-1][j+1][0])
            else:
                # 쉬다가 쉼, 달리다가 쉼, 지침지수 0인데 계속 쉼
                dp[i][j][0] = max(dp[i-1][j+1][0], dp[i-1][j+1][1], dp[i-1][j][0])
        else: # j == 1
            # 달리다가 달림, 쉬다가 달림
            dp[i][j][1] = max(dp[i-1][j-1][1], dp[i-1][j-1][0]) + D[i]
            # 달리다가 쉼, 쉬다가 쉼
            dp[i][j][0] = max(dp[i-1][j+1][1], dp[i-1][j+1][0])

print(dp[N][0][0])