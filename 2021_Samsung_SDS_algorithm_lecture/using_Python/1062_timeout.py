"""
input :
3 6
antarctica
antahellotica
antacartica

output :
2
"""

import sys
from itertools import combinations

input = sys.stdin.readline

N, K = map(int, input().split())

if K < 5:
    print(0)
    exit()

default_set = set("antic")

chars = []
alphabet_types = set()
for _ in range(N):
    data_refined = set(input().rstrip()[4:-4]) - default_set
    chars.append(data_refined)
    alphabet_types = alphabet_types | data_refined

max_val = 0
combi = list(combinations(alphabet_types, K-5))
for elimi in combi:
    tmp_val = 0
    for char_set in chars:
        if char_set.issubset(elimi):
            tmp_val += 1
    max_val = max(max_val, tmp_val)

print(max_val)
