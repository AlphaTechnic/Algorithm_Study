"""
input:
4 2
"""

import sys
import itertools
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
num_list = [i for i in range(1, N+1)]

for nums in list(itertools.combinations(num_list, M)):
    for num in nums:
        print(num, end=' ')
    print()