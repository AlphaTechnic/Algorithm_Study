"""
정확한 순위
input :
6 6
1 5
3 4
4 2
4 6
5 2
5 4
output :
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

print(graph)
reachable_to_x = [[] for _ in range(V + 1)]
x_can_go = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]


def dfs(start, cur):
    if len(graph[cur]) == 0:
        if not visited[cur]:
            x_can_go[start].append(cur)
            reachable_to_x[cur].append(start)
        return

    for nxt in graph[cur]:
        if not visited[nxt]:
            x_can_go[start].append(nxt)
            reachable_to_x[nxt].append(start)
            visited[nxt] = True

        dfs(start, nxt)


for i in range(1, V + 1):
    visited = [False for _ in range(V + 1)]
    visited[i] = True
    dfs(i, i)

cnt = 0
for x in range(1, V + 1):
    if len(reachable_to_x[x]) + len(x_can_go[x]) == V - 1:
        cnt += 1
print(cnt)
