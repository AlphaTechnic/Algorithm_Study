"""
input :
9
0
12345678
1
2
0
0
0
0
32

output :
0
1
2
12345678
0
"""

import sys
import heapq
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

data = []

N = int(input())
for _ in range(N):
    num = int(input())
    if num == 0:
        if len(data) == 0:
            print(0)
        else:
            print(heapq.heappop(data))
    else:
        heapq.heappush(data, num)
