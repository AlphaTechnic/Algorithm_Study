"""
input:
3 8
WEAK 10000
NORMAL 100000
STRONG 1000000
0
9999
10000
10001
50000
100000
500000
1000000
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, Q = map(int, input().rstrip().split())
upper_bounds = []
names = []

name, tmp = input().rstrip().split()
upper_bound = int(tmp)
names.append(name)
upper_bounds.append(upper_bound)
for _ in range(N-1):
    name, tmp = input().rstrip().split()
    upper_bound = int(tmp)
    if upper_bounds[-1] == upper_bound: continue
    names.append(name)
    upper_bounds.append(upper_bound)

query_list = []
for _ in range(Q):
    query_list.append(int(input()))

for query in query_list:
    print(names[bisect.bisect_left(upper_bounds, query)])