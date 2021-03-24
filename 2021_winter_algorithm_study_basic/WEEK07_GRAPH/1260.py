import sys
sys.stdin = open("input.txt", "r")

from collections import deque


def dfs(G, start):
    visited = list()
    s = list()
    s.append(start)
    while s:
        node = s.pop()
        if node not in visited:
            visited.append(node)
            if node not in G:
                return visited
            for item in G[node]:
                s.append(item)
    return visited


def bfs(G, start):
    visited = list()
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if node not in visited:
            visited.append(node)
            if node not in G:
                return visited
            q.extend(G[node])
    return visited


V, E, start = map(int, input().split())
graph = dict()
for _ in range(E):
    key, child = map(int, input().split())
    if key not in graph:
        graph[key] = list()
    if child not in graph:
        graph[child] = list()
    graph[key].append(child)
    graph[child].append(key)

for key in graph:
    graph[key].sort(reverse=True)
for item in dfs(graph, start):
    print(item, end=' ')

print()

for key in graph:
    graph[key].sort()
for item in bfs(graph, start):
    print(item, end=' ')