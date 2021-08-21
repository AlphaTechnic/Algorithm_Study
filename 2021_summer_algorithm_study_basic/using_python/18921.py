"""
input :
10
6 4 8
5 6 7
2 3 5
3 1 2
2 7 3
9 7 4
8 2 6
8 10 7
6 2 4

output :
24
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 10 ** 9 + 1


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

    # 종속시킬 엣지들 개수를 옮겨주기
    num_of_edges[a] += num_of_edges[b]
    parent[b] = a

    if height[a] == height[b]:
        height[a] += 1
    return True


if __name__ == '__main__':
    V = int(input())

    edges = list()
    for _ in range(V - 1):
        a, b, c = map(int, input().rstrip().split())
        edges.append((c, a, b))

    edges.sort(reverse=True)
    parent = [-1 for _ in range(V + 1)]
    height = [0 for _ in range(V + 1)]

    min_vals = [MAX for _ in range(V + 1)]
    num_of_edges = [0 for _ in range(V + 1)]
    max_val = 0
    for c, a, b in edges:
        min_vals[find(a)] = min(min_vals[find(a)], c)
        min_vals[find(b)] = min(min_vals[find(b)], c)
        union(a, b)
        num_of_edges[find(a)] += 1
        max_val = max(max_val, min_vals[find(a)] * num_of_edges[find(a)])
    print(max_val)
