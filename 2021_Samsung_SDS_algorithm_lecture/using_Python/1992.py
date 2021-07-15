"""
input :
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8

output :
23
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(a):
    if a == parent[a]: return parent[a]

    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)

    if pa < pb:
        parent[pb] = pa
        return True
    elif pa > pb:
        parent[pa] = pb
        return True
    else: # pa == pb
        return False


if __name__ == "__main__":
    N = int(input())
    parent = [i for i in range(N + 1)]

    M = int(input())

    edges = []
    for _ in range(M):
        a, b, w = map(int, input().rstrip().split())
        edges.append([a, b, w])

    edges.sort(key=lambda x: x[2])

    tot = 0
    cnt = 0
    for a, b, w in edges:
        if union(a, b):
            cnt += 1
            tot += w

        if cnt == N - 1:
            break

    print(tot)
