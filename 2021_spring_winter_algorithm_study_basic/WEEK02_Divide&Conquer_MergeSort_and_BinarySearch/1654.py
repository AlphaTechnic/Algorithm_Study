"""
input:
4 11
802
743
457
539

output:
200
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

low = 0
high = max(num_list)
ans = 0
while low <= high:
    mid = (low + high) // 2
    total = 0
    if mid == 0:
        ans = 1
        break
    for num in num_list:
        total += num // mid

    if total >= M:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)