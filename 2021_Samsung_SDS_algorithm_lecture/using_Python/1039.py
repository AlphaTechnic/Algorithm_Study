"""
input :
16375 1

output :
1
"""

import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

num_str, K = input().split()
digits = list(num_str)

print(digits)
print(indices)
