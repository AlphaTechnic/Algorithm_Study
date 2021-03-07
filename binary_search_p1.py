"""
정렬된 배열에서 특정 수의 개수 구하기
input :
7 2
1 1 2 2 2 2 3
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, target = map(int, input().split())
nums = list(map(int, input().split()))

s = bisect.bisect_left(nums, target)
e = bisect.bisect_right(nums, target)

if e - s == 0:
    print(-1)
else:
    print(e - s)
