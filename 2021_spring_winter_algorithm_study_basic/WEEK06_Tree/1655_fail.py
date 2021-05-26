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
data = []
for i in range(N):
    heapq.heappush(data, int(input()))
    print(heapq.nsmallest(i//2+1, data)[-1])
