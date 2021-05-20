"""
input :
2 10 3
16
32

output :
YES
3
"""

import sys
import heapq
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, H, LIMIT = map(int, input().rstrip().split())
data = []
for _ in range(N):
    heapq.heappush(data, -int(input()))

# 뿅망치를 쓰지 않아도 되는 상황
if -data[0] < H:
    print("YES")
    print(0)
    exit()

is_success = True
cnt = 0
while True:
    new_val = -math.ceil((-heapq.heappop(data)) // 2)
    if new_val >= -1: new_val = -1

    heapq.heappush(data, new_val)
    LIMIT -= 1
    cnt += 1
    if -data[0] < H: break
    if LIMIT == 0:
        is_success = False
        break

if is_success:
    print("YES")
    print(cnt)
else:
    print("NO")
    print(-data[0])
