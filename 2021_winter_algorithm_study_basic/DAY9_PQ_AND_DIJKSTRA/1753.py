import sys
sys.stdin = open("input.txt", "r")
import heapq

INF = int(1e9)


def dijkstra(start):
    que = []
    heapq.heappush(que, (0, start))
    distance[start] = 0

    while que:
        dist, cur = heapq.heappop(que)
        if distance[cur] < dist: # 이미 방문
            continue

        for target, weight in graph[cur]:
            cost = dist + weight
            if cost < distance[target]:
                distance[target] = cost
                heapq.heappush(que, (cost, target))


V, E = map(int, input().split())
K = int(input())
distance = [INF for _ in range(V+1)]

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(K)

for ans in distance[1:V+1]:
    if ans == INF:
        print("INF")
    else:
        print(ans)
