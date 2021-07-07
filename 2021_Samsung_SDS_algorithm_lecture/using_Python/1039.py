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
indices = [i for i in range(len(digits))]

print(digits)
print(indices)

indices_to_swap = list(combinations(indices, 2))

print(indices_to_swap)
for _ in range(K):
    for a, b in indices_to_swap:
        digits[a], digits[b] = digits[b], digits[a]