"""
input :
6 4
1 4
2 3
2 4
5 6
"""

import sys

sys.stdin = open("input.txt", "r")


# 경로 압축 기법 적용
def find_parent(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    group_a = find_parent(a)
    group_b = find_parent(b)
    if group_a < group_b:
        parent[b] = a
    else:
        parent[a] = b


V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

for i in range(E):
    a, b = map(int, input().split())
    union_parent(a, b)

print("각 원소가 속한 집합 : ")
for i in range(1, V + 1):
    print(find_parent(i), end=' ')
print("\n부모 테이블 : ")
for p in parent[1:]:
    print(p, end=' ')
