"""
특정 거리의 도시 찾기
input :
4 4 2 1
1 2
1 3
2 3
2 4
"""

import sys
import collections as col
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(S, target):
    q = col.deque()
    q.append((S, 0))
    visited[S] = True
    while q:
        now, depth = q.popleft()
        if depth == target: res.append(now)
        elif depth > target: break

        depth += 1
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, depth))


V, E, K, start = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

res = []
bfs(start, K)
res.sort()

if not res:
    print(-1)
else:
    for i in res:
        print(i, end=' ')

