"""
input :
10 15
5 1 3 5 10 7 4 9 2 8

output :
2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
accumulated_sum = [0]
tot = 0
for num in nums:
    tot += num
    accumulated_sum.append(tot)

a = 0
b = 1
ans = 100001
while a <= b < len(accumulated_sum):
    interval_sum = accumulated_sum[b] - accumulated_sum[a]
    if interval_sum < K:
        b += 1
    else:  # interval_sum >= K
        ans = min(ans, b - a)
        a += 1

if ans == 100001:
    print(0)
else:
    print(ans)