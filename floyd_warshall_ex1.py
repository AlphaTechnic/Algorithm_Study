import sys
sys.stdin = open("input.txt", "r")

INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF for _ in range(V + 1)] for _ in range(V+1)]
for i in range(V+1):
    graph[i][i] = 0

for _ in range(E):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dest, stopover = map(int, input().split())

# floyd warshall
for k in range(1, V+1):
    for s in range(1, V+1):
        for e in range(1, V+1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

ans = graph[1][stopover] + graph[stopover][dest]
if ans >= INF:
    print(-1)
else:
    print(ans)
