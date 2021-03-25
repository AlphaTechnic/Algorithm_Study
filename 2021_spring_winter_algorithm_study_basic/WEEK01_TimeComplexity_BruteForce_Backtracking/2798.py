"""
input :
10 500
93 181 245 214 315 36 185 138 216 295
"""

import sys
import itertools

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, target_num = map(int, input().split())
num_list = list(map(int, input().split()))

ans = -1
for a, b, c in list(itertools.combinations(num_list, 3)):
    total = a + b + c
    if ans < total <= target_num:
        ans = total
print(ans)
