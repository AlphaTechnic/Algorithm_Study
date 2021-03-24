import sys
sys.stdin = open("input.txt", "r")

import heapq


INF = 1e9
r, c = map(int, input().split())
mov = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dist = [[INF for _ in range(c)] for _ in range(r)]


def dijkstra(r, c):
    que = []

    heapq.heappush(que, [blueprint[0][0], 0, 0]) # dist, r, c
    dist[0][0] = blueprint[0][0]
    blueprint[0][0] = -2

    while que:
        cur_dist, cur_r, cur_c = heapq.heappop(que)

        if dist[cur_r][cur_c] < cur_dist:
            continue

        for mov_r, mov_c in mov:
            nxt_r = cur_r + mov_r
            nxt_c = cur_c + mov_c
            if 0 <= nxt_r < r and 0 <= nxt_c < c:
                if blueprint[nxt_r][nxt_c] != -1 and blueprint[nxt_r][nxt_c] != '_':
                    if dist[nxt_r][nxt_c] > blueprint[nxt_r][nxt_c] + cur_dist:
                        dist[nxt_r][nxt_c] = blueprint[nxt_r][nxt_c] + cur_dist
                        heapq.heappush(que, [dist[nxt_r][nxt_c], nxt_r, nxt_c])
                        blueprint[nxt_r][nxt_c] = '_'



blueprint = []
for _ in range(r):
    blueprint.append(list(map(int, input().split())))

if blueprint[0][0] == -1:
    print(-1)
else:
    dijkstra(r, c)
    if dist[r-1][c-1] == INF:
        print(-1)
    else:
        print(dist[r-1][c-1])
