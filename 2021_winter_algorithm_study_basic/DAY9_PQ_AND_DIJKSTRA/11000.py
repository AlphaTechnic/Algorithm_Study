import sys
sys.stdin = open("input.txt", "r")
import heapq

N = int(input())
lectures = []

for i in range(N):
    lectures.append(list(map(int, input().split())))
lectures.sort()

rooms = []
heapq.heappush(rooms, lectures[0][1])

for i in range(1, N):
    if rooms[0] <= lectures[i][0]:
        heapq.heappop(rooms)
        heapq.heappush(rooms, lectures[i][1])
    else:
        heapq.heappush(rooms, lectures[i][1])

print(len(rooms))