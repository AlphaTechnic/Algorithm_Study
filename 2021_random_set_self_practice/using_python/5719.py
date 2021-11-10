"""
input :
7 9
0 6
0 1 1
0 2 1
0 3 2
0 4 3
1 5 2
2 6 4
3 6 2
4 6 4
5 6 1

output :
5
"""
import sys
from collections import deque
from collections import defaultdict
from heapq import *

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

INF = 10 ** 9


def dijkstra(S):
    pq = []
    heappush(pq, (0, S))
    dist[S] = 0

    while pq:
        cumulative_dist, cur_nd = heappop(pq)
        if dist[cur_nd] < cumulative_dist: continue

        for nxt_c, nxt_nd in graph[cur_nd]:
            new_dist = cumulative_dist + nxt_c
            if new_dist >= dist[nxt_nd]: continue

            dist[nxt_nd] = new_dist
            heappush(pq, (new_dist, nxt_nd))


def chk_min_path(E):  # bfs 기반
    que = deque()
    que.append((dist[E], E))
    while que:
        cumulative_dist, cur_nd = que.popleft()
        for nxt_c, nxt_nd in graph_reverse[cur_nd]:
            if dist[nxt_nd] != dist[cur_nd] - nxt_c: continue
            if min_path_chk[nxt_nd][cur_nd]: continue

            min_path_chk[nxt_nd][cur_nd] = True
            if cur_nd == START: continue
            que.append((dist[nxt_nd], nxt_nd))


def dijkstra2(S):
    pq = []
    heappush(pq, (0, S))
    dist[S] = 0

    while pq:
        cumulative_dist, cur_nd = heappop(pq)
        if dist[cur_nd] < cumulative_dist: continue

        for nxt_c, nxt_nd in graph[cur_nd]:
            new_dist = cumulative_dist + nxt_c
            if new_dist >= dist[nxt_nd]: continue
            if min_path_chk[cur_nd][nxt_nd]: continue  # 이거 한 줄 추가된 것 뿐.

            dist[nxt_nd] = new_dist
            heappush(pq, (new_dist, nxt_nd))


if __name__ == "__main__":
    while True:
        V, E = map(int, input().rstrip().split())
        if V == 0: break
        START, END = map(int, input().rstrip().split())

        graph = defaultdict(list)
        graph_reverse = defaultdict(list)
        for _ in range(E):
            a, b, c = map(int, input().rstrip().split())
            graph[a].append((c, b))
            graph_reverse[b].append((c, a))

        # 최단 경로의 길이 구하기
        dist = [INF for _ in range(V)]
        dijkstra(START)
        # 최단 경로 구하기 (최단 경로를 이루는 edge들 제거)
        min_path_chk = [[False for _ in range(V)] for _ in range(V)]
        chk_min_path(END)
        # 최단 경로 edge 제거한 상태의 그래프에서 최단 경로 구하기
        dist = [INF for _ in range(V)]
        dijkstra2(START)

        if dist[END] == INF:
            print(-1)
        else:
            print(dist[END])
