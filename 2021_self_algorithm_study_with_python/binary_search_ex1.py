"""
input :
5
8 3 7 9 2
3
5 7 9
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

def binary_search(arr_sorted, target):
    i = bisect.bisect_left(arr_sorted, target)
    return i < len(arr_sorted) and arr_sorted[i] == target


N = int(input())
data = sorted(list(map(int, input().split())))
M = int(input())
query = list(map(int, input().split()))

for q in query:
    if binary_search(data, q):
        print('yes', end=' ')
    else:
        print("no", end=' ')