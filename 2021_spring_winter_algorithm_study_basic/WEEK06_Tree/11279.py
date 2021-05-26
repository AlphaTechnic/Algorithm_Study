"""
input :
13
0
1
2
0
0
3
2
1
0
0
0
0
0

output :
0
2
1
3
2
1
0
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
            print(-heapq.heappop(data))
    else:
        heapq.heappush(data, -num)
