"""
input :
4 2
4 2
3 1

output :
3 1 4 2
"""
import sys
# from collections import deque
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    graph = [[] for _ in range(N + 1)]
    indeg = [0 for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        indeg[b] += 1

    min_heap = []
    #que = deque()
    for i in range(1, N + 1):
        if indeg[i] == 0:
            heapq.heappush(min_heap, i)
    while len(min_heap) != 0:
        cur = heapq.heappop(min_heap)
        print(cur, end=' ')
        for nxt in graph[cur]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                heapq.heappush(min_heap, nxt)
