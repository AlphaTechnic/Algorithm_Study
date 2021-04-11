"""
input :
4 7
6 13
4 8
3 6
5 12

ouput :
14
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
weights = [0]
vals = [0]
for _ in range(N):
    w, v = map(int, input().split())
    weights.append(w)
    vals.append(v)

# 물건을 1부터 N까지 하나씩 바라보면서
# dp[k][i] = 목표가 k인 상황에서 가방에 채울 수 있는 val의 최댓값
dp = [[0 for _ in range(N + 1)] for _ in range(K + 1)]
for k in range(1, K + 1):
    for i in range(1, N + 1):
        if k - weights[i] >= 0:  # 현재 보고있는 물건을 추가하려면, 아래의 dp 값을 비교해 큰걸 가져온다.
            dp[k][i] = max(dp[k][i-1], dp[k-weights[i]][i-1] + vals[i])
        else: # 현재 보고 있는 물건을 추가하지 못하면, 직전에 바라본 dp 값을 가져와야 한다.
            dp[k][i] = dp[k][i-1]

print(dp[K][N])
