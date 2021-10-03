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
from collections import defaultdict
from heapq import *
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(S):
    pq = []
    dist[S] = 0

    heappush(pq, (0, S))
    while pq:
        cum_dist, cur_nd = heappop(pq)
        if cum_dist > dist[cur_nd]: continue

        for nc, new_nd in graph[cur_nd]:
            new_dist = dist[cur_nd] + nc
            if new_dist > dist[new_nd]: continue

            dist[new_nd] = new_dist
            heappush(pq, (new_dist, new_nd))


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    S = int(input())
    graph = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((c, b))

    dist = [INF for _ in range(V + 1)]
    dijkstra(S)

    for nd in range(1, V + 1):
        print(dist[nd]) if dist[nd] != INF else print("INF")
