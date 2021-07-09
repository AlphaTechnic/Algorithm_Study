"""
input :
10 5
1 2 3 4 2 5 3 1 1 2

output :
3
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
accumulated_sum = [0]
tot = 0
for num in nums:
    tot += num
    accumulated_sum.append(tot)

a = 0
b = 1
ans = 0
while True:
    if b >= len(accumulated_sum): break

    interval_sum = accumulated_sum[b] - accumulated_sum[a]
    if interval_sum < M:
        b += 1
    elif interval_sum > M:
        a += 1
    else:  # interval_sum == M
        a += 1
        ans += 1

print(ans)