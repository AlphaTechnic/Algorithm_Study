"""
input :
3
1 2 3
4 5 6
4 9 0

output :
18 6
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
if N == 1:
    nums = list(map(int, input().rstrip().split()))
    print(max(nums), min(nums))
    exit()

min_dp = []
for _ in range(N):
    min_dp.append(list(map(int, input().rstrip().split())))

max_dp = [[0 for _ in range(3)] for _ in range(N)]
for r in range(N):
    for c in range(3):
        max_dp[r][c] = min_dp[r][c] = min_dp[r][c]

for r in range(1, N):
    min_dp[r][0] = min(min_dp[r-1][0] + min_dp[r][0], min_dp[r-1][1] + min_dp[r][0])
    min_dp[r][1] = min(map(lambda x: x + min_dp[r][1], min_dp[r-1]))
    min_dp[r][2] = min(min_dp[r-1][1] + min_dp[r][2], min_dp[r-1][2] + min_dp[r][2])
    max_dp[r][0] = max(max_dp[r - 1][0] + max_dp[r][0], max_dp[r - 1][1] + max_dp[r][0])
    max_dp[r][1] = max(map(lambda x: x + max_dp[r][1], max_dp[r-1]))
    max_dp[r][2] = max(max_dp[r - 1][1] + max_dp[r][2], max_dp[r - 1][2] + max_dp[r][2])

print(max(max_dp[N - 1]), min(min_dp[N - 1]))