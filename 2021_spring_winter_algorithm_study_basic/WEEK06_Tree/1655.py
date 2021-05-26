"""
input :
7
1
5
2
10
-99
7
5

output :
1
1
2
2
2
2
5
"""

import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
LESS = []  # max heap으로 관리
GREATER = []  # min heap으로 관리
res = []
for _ in range(N):
    num = int(input())

    if len(LESS) == len(GREATER): heapq.heappush(LESS, (-num, num))
    else: heapq.heappush(GREATER, (num, num))

    if len(GREATER) != 0 and LESS[0][1] > GREATER[0][1]:
        _, LESS_TOP = heapq.heappop(LESS)
        _, GREATER_TOP = heapq.heappop(GREATER)
        heapq.heappush(LESS, (-GREATER_TOP, GREATER_TOP))
        heapq.heappush(GREATER, (LESS_TOP, LESS_TOP))
    res.append(LESS[0][1])

for i in res:
    print(i)
