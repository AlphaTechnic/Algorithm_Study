"""
input :
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = int(1e9)
V = int(input())
E = int(input())

graph = [[INF for i in range(V+1)] for _ in range(V+1)]
for i in range(V+1):
    graph[i][i] = 0

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a][b] = w

for k in range(V+1):
    for a in range(V+1):
        for b in range(V+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, V+1):
    for b in range(1, V+1):
        if graph[a][b] == INF:
            print("INF", end=" ")
        else:
            print(graph[a][b], end=" ")
    print()

