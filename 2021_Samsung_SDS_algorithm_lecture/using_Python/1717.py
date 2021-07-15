"""
input :
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

output :
NO
NO
YES
"""

import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(a):
    if parent[a] == a: return a

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb: parent[pb] = pa
    else: parent[pa] = pb


if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())
    parent = [i for i in range(N + 1)]

    for _ in range(Q):
        q, a, b = map(int, input().rstrip().split())

        if q == 0:
            union(a, b)
        else:  # q = 1
            if find(a) == find(b):
                print("YES")
            else:
                print("NO")
