"""
input :
4 7
20 15 10 17
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, target = map(int, input().rstrip().split())
height_list = list(map(int, input().rstrip().split()))

ans = 0
high = max(height_list)
low = 0
while low <= high:
    mid = (low + high) // 2
    total = 0
    for height in height_list:
        if height > mid:
            total += height - mid

    if total < target:
        high = mid - 1
    elif total >= target:
        ans = mid
        low = mid + 1

print(ans)