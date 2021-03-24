import sys
from collections import deque

sys.setrecursionlimit(2000000)

N, Q = map(int, sys.stdin.readline().split())

origin = [0, 1] + [int(sys.stdin.readline()) for _ in range(N - 1)]
parent = [i for i in range(N + 1)]

query = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N + Q - 1)]


def get_parent(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = get_parent(parent[x])
        return parent[x]


def union(x, y):
    a, b = get_parent(x), get_parent(y)

    if a != b:
        parent[a] = b


result = deque([])
for curQ in query[::-1]:
    if curQ[0] == 0:
        union(curQ[1], origin[curQ[1]])
    else:
        if get_parent(curQ[1]) == get_parent(curQ[2]):
            result.appendleft("YES")
        else:
            result.appendleft("NO")

print('\n'.join(result))