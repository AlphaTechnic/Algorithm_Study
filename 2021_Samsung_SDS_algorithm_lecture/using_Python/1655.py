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

LARGE_DATA_SET = [] # min heap으로 관리
SMALL_DATA_SET = [] # max heap으로 관리
N = int(input())

ans = []
for _ in range(N):
    num = int(input())

    if len(LARGE_DATA_SET) == len(SMALL_DATA_SET):
        heapq.heappush(SMALL_DATA_SET, -num)
    else:  # actually len(LARGE_DATA_SET) == len(SMALL_DATA_SET) - 1
        heapq.heappush(LARGE_DATA_SET, num)

    if len(LARGE_DATA_SET) != 0 and LARGE_DATA_SET[0] < -SMALL_DATA_SET[0]:
        to_small = -heapq.heappop(LARGE_DATA_SET)  # small로 들어갈 거라 minus
        to_large = -heapq.heappop(SMALL_DATA_SET)  # small에서 나온 거라 minus
        heapq.heappush(LARGE_DATA_SET, to_large)
        heapq.heappush(SMALL_DATA_SET, to_small)

    ans.append(str(-SMALL_DATA_SET[0]))

for num in ans:
    print(num)