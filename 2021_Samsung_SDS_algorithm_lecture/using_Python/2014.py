"""
4 19
2 3 5 7

27
"""

import sys
import heapq

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

k, n = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

heap_arr = [num for num in arr]
heapq.heapify(heap_arr)
head = -1
for _ in range(n):
    head = heapq.heappop(heap_arr)
    for num in arr:
        to_push = head * num
        heapq.heappush(heap_arr, min(to_push, 1 << 31))
        if head % num == 0:
            break

print(head)

