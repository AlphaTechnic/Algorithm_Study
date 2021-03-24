"""
input :
7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find_parent(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    set_a = find_parent(a)
    set_b = find_parent(b)
    if set_a < set_b:
        parent[set_b] = set_a
    else:
        parent[set_a] = set_b


V, E = map(int, input().split())
parent = [i for i in range(V+1)]
total = 0

edges = []
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total += cost

print(total)