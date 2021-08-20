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


def find(x):
    if parent[x] == -1: return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a == b: return False

    if a < b: a, b = b, a
    parent[b] = a

    if height[a] == height[b]:
        height[a] += 1

    return True


def kruskal():
    global min_val
    edges.sort()
    for c, a, b in edges:
        if union(a, b):  # 사이클 없음
            min_val += c


if __name__ == "__main__":
    V = int(input())
    E = int(input())

    graph = dict()
    for i in range(V + 1):
        graph[i] = list()

    edges = list()
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
        edges.append((c, a, b))


    parent = [-1 for _ in range(V + 1)]
    height = [0 for _ in range(V + 1)]
    min_val = 0
    kruskal()
    print(min_val)
