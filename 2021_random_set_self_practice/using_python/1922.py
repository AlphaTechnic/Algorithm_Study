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

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def find(a):
    if par[a] == -1:
        return a
    par[a] = find(par[a])
    return par[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if height[a] < height[b]:
        a, b = b, a
    par[b] = a
    if height[a] == height[b]:
        height[a] += 1

    return True


def kruskal():
    edges.sort()
    tot = 0
    for c, a, b in edges:
        if union(a, b):
            tot += c
    return tot


if __name__ == "__main__":
    V = int(input())
    E = int(input())
    edges = []
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        edges.append((c, a, b))

    par = [-1 for _ in range(V + 1)]
    height = [0 for _ in range(V + 1)]
    print(kruskal())
