"""
input :
7 3 4

output :
3
6
2
7
1
5
4
"""

import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K, M = map(int, input().split())
dq = deque([i for i in range(1, N+1)])

cnt = 0
dir_flag = 1
while True:
    if len(dq) == 0:
        break

    if cnt == M:  # 회전방향 change
        dir_flag *= -1
        cnt = 0

    if dir_flag == 1:
        dq.rotate(-K + 1)
        print(dq.popleft())
    else:
        dq.rotate(K - 1)
        print(dq.pop())
    cnt += 1