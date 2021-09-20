"""
input :
15
1 2
1 3
2 4
3 7
6 2
3 8
4 9
2 5
5 11
7 13
10 4
11 15
12 5
14 7
6
6 11
10 9
2 6
7 6
8 13
8 15

output :
2
4
2
1
3
1
"""
import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(cur, dep):
    vis[cur] = True
    depth[cur] = dep
    for nxt in graph[cur]:
        if vis[nxt]: continue

        par[nxt] = cur
        dfs(nxt, dep + 1)


def LCA(a, b):
    if depth[b] > depth[a]:
        a, b = b, a

    while depth[a] != depth[b]:
        a = par[a]
    while a != b:
        a = par[a]
        b = par[b]
    return a


if __name__ == "__main__":
    V = int(input())

    graph = defaultdict(list)
    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    depth = [0 for _ in range(V + 1)]
    vis = [False for _ in range(V + 1)]
    par = [-1 for _ in range(V + 1)]
    dfs(1, 1)

    Q = int(input())
    cache = dict()
    for _ in range(Q):
        a, b = map(int, input().rstrip().split())
        if (a, b) in cache:
            print(cache[(a, b)])
            continue

        cache[(a, b)] = cache[(b, a)] = LCA(a, b)
        print(cache[(a, b)])
