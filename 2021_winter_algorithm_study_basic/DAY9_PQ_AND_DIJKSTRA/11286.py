import sys
sys.stdin = open("input.txt", "r")

import heapq

N = int(sys.stdin.readline())
min_heap = []

for _ in range(N):
    operation = int(sys.stdin.readline())
    if operation == 0:
        if len(min_heap) != 0:
            _, min_val = heapq.heappop(min_heap)
            print(min_val)
        else:
            print(0)
    else:
        heapq.heappush(min_heap, (abs(operation), operation))
