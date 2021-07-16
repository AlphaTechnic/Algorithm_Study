"""
input :
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

output :
0
2
3
7
INF
"""

import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


INF = 10**8


def dijkstra(S):
    min_heap = []
    distance[S] = 0
    heapq.heappush(min_heap, [0, S])

    while len(min_heap) != 0:
        w, cur = heapq.heappop(min_heap)
        if distance[cur] < w: continue

        for w, nxt in graph[cur]:
            new_cost = distance[cur] + w
            if new_cost > distance[nxt]: continue

            distance[nxt] = new_cost
            heapq.heappush(min_heap, [new_cost, nxt])


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    S = int(input())

    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b, w = map(int, input().rstrip().split())
        graph[a].append([w, b])

    distance = [INF for _ in range(V + 1)]

    dijkstra(S)

    for i in range(1, V + 1):
        if distance[i] != INF:
            print(distance[i])
        else:
            print("INF")
