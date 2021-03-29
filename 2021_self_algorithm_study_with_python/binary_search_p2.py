"""
고정점 찾기
input :
7
-15 -4 2 8 9 13 15

output :
2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))

def binary_search():
    l = 0
    r = N - 1
    while l <= r:
        mid = (l + r) // 2
        if mid == num_list[mid]:
            print(mid)
            return
        elif mid > num_list[mid]:
            l = mid + 1
        else:  # mid < num_list[mid]
            r = mid - 1
    print(-1)
    return

binary_search()
