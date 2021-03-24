import sys
sys.stdin = open("input.txt", "r")

INF = int(1e9)


def bellmanford(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur, nxt, cost = edges[j]
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == N-1:
                    return True
    return False

N, M = map(int, input().split())
dist = [INF for _ in range(N+1)]
edges = []
for _ in range(M):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

neg_cycle = bellmanford(1)

if neg_cycle is True:
    print("-1")
else:
    for i in range(2, N+1):
        if dist[i] == INF:
            print("-1")
        else:
            print(dist[i])
