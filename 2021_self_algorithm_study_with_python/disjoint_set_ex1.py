"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
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


def is_same(a, b):
    if find_parent(a) == find_parent(b):
        print("YES")
    else:
        print("NO")


N, M = map(int, input().split())
parent = [i for i in range(N + 1)]

for _ in range(M):
    oper, a, b = map(int, input().split())
    if oper == 0:  # 팀 합치기 연산
        union_parent(a, b)
    elif oper == 1:  # 같은 팀 여부 확인 연산
        is_same(a, b)
