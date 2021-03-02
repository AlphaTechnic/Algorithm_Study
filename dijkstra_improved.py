import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
import heapq
INF = int(1e9)


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # heqp에서 꺼냈는데 이미 처리된 놈이면 continue
        if distance[now] < dist:
            continue

        for nxt, weight in graph[now]:
            cost = distance[now] + weight
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))


V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF for _ in range(V + 1)]

for _ in range(E):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

dijkstra(start)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])