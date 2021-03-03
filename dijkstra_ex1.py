import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(src):
    q = []
    heapq.heappush(q, (0, src))
    distance[start] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if dist > distance[cur]:
            continue

        for nxt, w in graph[cur]:
            cost = dist + w
            if distance[nxt] > cost:
                distance[nxt] = cost
                heapq.heappush(q, (cost, nxt))


V, E, start = map(int, input().split())
distance = [INF for _ in range(V + 1)]
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    s, e, weight = map(int, input().split())
    graph[s].append((e, weight))

dijkstra(start)
cnt = 0
max_dist = 0
for d in distance:
    if d != INF:
        cnt += 1
        max_dist = max(d, max_dist)

print(cnt - 1, max_dist) # 시작노드 제외 : cnt - 1
