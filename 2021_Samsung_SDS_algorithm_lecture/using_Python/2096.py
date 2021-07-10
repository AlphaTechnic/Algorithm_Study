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

min_dp = list(map(int, input().rstrip().split()))
max_dp = [0, 0, 0]
for i in range(3):
    max_dp[i] = min_dp[i]

for _ in range(1, N):
    data = list(map(int, input().rstrip().split()))
    tmp0 = min(min_dp[0] + data[0], min_dp[1] + data[0])
    tmp1 = min(min_dp) + data[1]
    tmp2 = min(min_dp[1] + data[2], min_dp[2] + data[2])
    min_dp[0], min_dp[1], min_dp[2] = tmp0, tmp1, tmp2

    tmp0 = max(max_dp[0] + data[0], max_dp[1] + data[0])
    tmp1 = max(max_dp) + data[1]
    tmp2 = max(max_dp[1] + data[2], max_dp[2] + data[2])
    max_dp[0], max_dp[1], max_dp[2] = tmp0, tmp1, tmp2

print(max(max_dp), min(min_dp))