"""
input :
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8

output :
23
"""

import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def prim(S):
    min_heap = []
    visited[S] = True

    for i in graph[S]:
        heapq.heappush(min_heap, i)

    tot = 0
    cnt = 0
    while len(min_heap) != 0:
        w, cur_node = heapq.heappop(min_heap)
        if visited[cur_node]: continue

        visited[cur_node] = True
        cnt += 1
        tot += w
        for nxt_node in graph[cur_node]:
            heapq.heappush(min_heap, nxt_node)

        if cnt == N - 1:
            return tot
    return tot


if __name__ == "__main__":
    N = int(input())
    M = int(input())

    graph = dict()
    for i in range(1, N + 1):
        graph[i] = []

    visited = [False for _ in range(N + 1)]
    for _ in range(M):
        a, b, w = map(int, input().rstrip().split())
        graph[a].append([w, b])
        graph[b].append([w, a])

    print(prim(1))