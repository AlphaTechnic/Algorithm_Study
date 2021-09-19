"""
input :
5 10 2
1 2 2
1 3 7
1 4 5
1 5 6
2 4 2
2 3 4
3 4 6
3 5 8
5 2 4
5 4 1

output :
-1
10
7
5
14
"""
import sys
from collections import defaultdict
import heapq
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
INF = 10 ** 9


def dijkstra(s, k):
    min_heap = list()
    heapq.heappush(min_heap, (0, 1))
    dist[s][0] = 0
    while min_heap:
        cumulative_dist, cur_nd = heapq.heappop(min_heap)
        for nxt_c, nxt_nd in graph[cur_nd]:
            new_dist = cumulative_dist + nxt_c
            if dist[nxt_nd][k - 1] <= new_dist: continue

            dist[nxt_nd][k - 1] = new_dist
            dist[nxt_nd].sort()
            heapq.heappush(min_heap, (new_dist, nxt_nd))


if __name__ == "__main__":
    V, E, K = map(int, input().rstrip().split())

    dist = [[INF for _ in range(K)] for _ in range(V + 1)]
    graph = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((c, b))

    dijkstra(1, K)
    for i in range(1, V + 1):
        if dist[i][K - 1] != INF:
            print(dist[i][K - 1])
        else:
            print(-1)
