"""
여행계획
input :
5 4
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
2 3 4 3
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
    A = find_parent(a)
    B = find_parent(b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


N, _ = map(int, input().split())
graph = [[0 for _ in range(N + 1)]]
for _ in range(N):
    graph.append([0] + list(map(int, input().split())))
query = list(set(map(int, input().split())))

parent = [i for i in range(N + 1)]
for r in range(1, N + 1):
    for c in range(r, N + 1):
        if graph[r][c] == 1:
            union_parent(r, c)

p = find_parent(query[0])
for i in query[1:]:
    parent_of_i = find_parent(i)
    if p != parent_of_i:
        print("NO")
        break
else:
    print("YES")
