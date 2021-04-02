"""
input :
7 10
3
8
3
6
9
2
4

output :
8
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = []
for _ in range(N):
    num_list.append(int(input()))

high = M * max(num_list)
low = 0
ans = 0
while low <= high:
    mid = (low + high) // 2
    total = 0
    for num in num_list:
        total += mid // num

    if total >= M:
        ans = mid
        high = mid - 1
    else:
        low = mid + 1

print(ans)
