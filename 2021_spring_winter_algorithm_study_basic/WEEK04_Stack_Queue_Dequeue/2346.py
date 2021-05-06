"""
input :
5
3 2 1 -3 -1

output :
1 4 5 3 2
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
move = list(map(int, input().split()))
move_dq = deque(move)
for ind, data in enumerate(move):
    move_dq[ind] = (data, ind + 1)

while True:
    data, ind = move_dq.popleft()
    print(ind, end=' ')
    if len(move_dq) == 0:
        break
    if data > 0:
        move_dq.rotate((-data + 1) % len(move_dq))
    else:
        move_dq.rotate((-data) % len(move_dq))
