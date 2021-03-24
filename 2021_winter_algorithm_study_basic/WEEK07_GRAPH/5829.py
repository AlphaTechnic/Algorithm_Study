import sys
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())

port = [[0, 0] for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
dir = [0 for _ in range(M)]

for i in range(1, N+1):
    port[i][0], port[i][1] = map(int, input().split())

for i, char in enumerate(input().split()):
    if char == 'L':
        dir[i] = 0
    else:
        dir[i] = 1

cur = 1
temp1 = 1

for i in range(K):
    if dp[cur] > 0:
        cur = dp[cur]
    else:
        for j in range(M):
            temp = port[temp1][dir[j]]
            temp1 = temp
        dp[cur] = temp1
        cur = temp1

print(cur)