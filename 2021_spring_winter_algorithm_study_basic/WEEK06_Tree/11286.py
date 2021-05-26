"""
input:
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0

output :
-1
1
0
-1
-1
1
1
-2
2
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
            print(heapq.heappop(data)[1])
    else:
        heapq.heappush(data, (abs(num), num))
