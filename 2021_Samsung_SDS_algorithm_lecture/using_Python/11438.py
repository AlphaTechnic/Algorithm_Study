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
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


LOG = 21  # 2^20 = 1,000,000


def gen_depth_by_bfs(S):
    visited = [False for _ in range(N + 1)]
    que = deque()
    que.append(S)
    visited[S] = True
    depth[S] = 1

    while len(que) != 0:
        cur = que.popleft()

        for nxt in graph[cur]:
            if visited[nxt]: continue

            visited[nxt] = True
            depth[nxt] = depth[cur] + 1
            parent[nxt][0] = cur

            que.append(nxt)


def set_parent():
    for dep_pow in range(1, LOG):
        for node in range(1, N + 1):
            #  pn = p[node][2^depth]
            parent[node][dep_pow] = parent[parent[node][dep_pow - 1]][dep_pow - 1]


def lca(a, b):
    # b가 더 깊도록 셋팅
    if depth[a] > depth[b]:
        a, b = b, a

    # depth가 같도록 셋팅
    for dep_pow in range(LOG - 1, -1, -1):
        # if depth[b] - depth[a] >= (1 << dep_pow):
        #     b = parent[b][dep_pow]
        if (depth[b] - depth[a]) & (1 << dep_pow) == (1 << dep_pow):
            b = parent[b][dep_pow]

    # 부모가 같아지도록
    if a == b:
        return a
    for dep_pow in range(LOG - 1, -1, -1):
        if parent[a][dep_pow] != parent[b][dep_pow]:
            a = parent[a][dep_pow]
            b = parent[b][dep_pow]

    return parent[a][0]


if __name__ == "__main__":
    N = int(input())
    graph = dict()
    for i in range(1, N + 1):
        graph[i] = []

    for _ in range(N - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    depth = [0 for _ in range(N + 1)]
    parent = [[0 for i in range(LOG)] for _ in range(N + 1)]
    gen_depth_by_bfs(1)
    set_parent()

    M = int(input())
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        print(lca(a, b))
