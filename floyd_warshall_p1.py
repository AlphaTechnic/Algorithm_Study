"""
플로이드
input :
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10 ** 9

V = int(input())
E = int(input())

graph = [[INF for _ in range(V + 1)] for _ in range(V + 1)]
for i in range(V + 1):
    graph[i][i] = 0

for _ in range(E):
    a, b, cost = map(int, input().split())
    if cost < graph[a][b]:
        graph[a][b] = cost

for k in range(1, V + 1):
    for r in range(1, V + 1):
        for c in range(1, V + 1):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

for r in range(1, V + 1):
    for c in range(1, V + 1):
        if graph[r][c] == INF:
            print(0, end=' ')
            continue
        print(graph[r][c], end=' ')
    print()
