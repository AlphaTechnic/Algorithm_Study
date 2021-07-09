"""
input :
5
4
1 3 1 2
3
1 3 2

output :
7
"""

import sys
from itertools import combinations
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

T = int(input())
N = int(input())
A = list(map(int, input().rstrip().split()))
M = int(input())
B = list(map(int, input().rstrip().split()))

accumul_sum_A = [0]
accumul_sum_B = [0]
tot = 0
for num in A:
    tot += num
    accumul_sum_A.append(tot)

tot = 0
for num in B:
    tot += num
    accumul_sum_B.append(tot)

combi_A = list(combinations(accumul_sum_A, 2))
combi_B = list(combinations(accumul_sum_B, 2))


B_sums = dict()
for b1, b2 in combi_B:
    if b2 - b1 in B_sums:
        B_sums[b2 - b1] += 1
    else:
        B_sums[b2 - b1] = 1

tot = 0
for a1, a2 in combi_A:
    sum_A = a2 - a1
    target_B_val = T - sum_A
    if target_B_val in B_sums:
        tot += B_sums[target_B_val]

print(tot)

