"""
input :
4 2
9 7 9 1

output :
1 7
1 9
7 1
7 9
9 1
9 7
9 9
"""

import sys
from itertools import permutations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))

ans = list(set(list(permutations(nums, M))))
ans.sort()

for ele in ans:
    for i in ele:
        print(i, end=' ')
    print()


