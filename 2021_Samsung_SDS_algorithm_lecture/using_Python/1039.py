"""
input :
132 3

output :
312
"""

import sys
import copy
from collections import deque
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

num_str, K = input().split()

if len(num_str) == 1:
    print(-1)
    exit()

digits = list(num_str)
indices = [i for i in range(len(digits))]
combi = list(combinations(indices, 2))

que = deque()
que.append(digits)
lv = 0
while lv < int(K):
    qsize = len(que)
    for _ in range(qsize):
        num = que.popleft()
        for a, b in combi:
            num[a], num[b] = num[b], num[a]

            if num[0] == '0':
                num[a], num[b] = num[b], num[a]
                continue

            tmp = copy.deepcopy(num)
            if tmp not in que:  # backtraking
                que.append(tmp)
            num[a], num[b] = num[b], num[a]

    lv += 1

if len(que) == 0:
    print(-1)
    exit()

max_val = 0
for ele in que:
    max_val = max(int("".join(ele)), max_val)
print(max_val)
