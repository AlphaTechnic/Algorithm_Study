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


V = int(input())
E = int(input())
distance = [INF for _ in range(V+1)]

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

start, end = map(int, input().split())

dijkstra(start)

print(distance[end])