"""
input:
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4
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

V, E = map(int, input().split())
edges = []
parent = [i for i in range(V+1)]
for _ in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()
total = 0
max_val = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total += cost
        max_val = cost # cost는 오름차순으로 들어온다.

print(total - max_val)
