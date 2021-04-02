"""
input :
4
120 110 140 150
485
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().rstrip().split()))
budget = int(input())

ans = 0
if sum(num_list) <= budget:
    ans = max(num_list)
    print(ans)
    exit()

low = 0
high = max(num_list)
while low <= high:
    mid = (low + high) // 2
    total = 0
    for num in num_list:
        if num > mid:
            total += mid
        else:
            total += num

    if total <= budget:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
