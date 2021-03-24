"""
input :
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""
import collections as col
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

V, E = map(int, input().split())
indegree = [0 for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    res = []
    q = col.deque()

    for i in range(1, V + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        res.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in res:
        print(i, end=' ')


topology_sort()
