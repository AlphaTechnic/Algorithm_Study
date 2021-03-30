"""
floyd 최단경로로 해결

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
INF = int(10e9)

V, E = map(int, input().split())

graph = [[INF for _ in range(V + 1)] for _ in range(V + 1)]
for i in range(V + 1):
    graph[i][i] = 0
for _ in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

cnt = 0
for a in range(1, V+1):
    for b in range(1, V+1):
        if graph[a][b] == INF and graph[b][a] == INF: break
    else:
        cnt += 1

print(cnt)
