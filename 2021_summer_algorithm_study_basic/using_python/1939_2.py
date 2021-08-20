"""
input :
3 3
1 2 2
3 1 3
2 3 2
1 3

output :
3
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find(x):
    if parent[x] == -1:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if height[a] < height[b]:
        a, b = b, a
    parent[b] = a

    if height[a] == height[b]:
        height[a] += 1

    return True


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    edges = []
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
        edges.append((c, a, b))
    S, END = map(int, input().rstrip().split())

    parent = [-1 for _ in range(V + 1)]
    height = [0 for _ in range(V + 1)]

    edges.sort(reverse=True)
    for edge in edges:
        union(edge[1], edge[2])
        if find(S) == find(END):
            print(edge[0])
            break
