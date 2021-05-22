"""
input :
6 3 2
3000 100
1500 200
1000 500
1500 100
1500 100
1500 100

output :
4
"""

import sys
import heapq
from collections import deque
# line은 queue로 관리, head는 heap으로 관리

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def change_sign(num):
    return -int(num)


N, LINE_NUM, DEKA = map(int, input().rstrip().split())

LINES = [deque() for _ in range(LINE_NUM)]
ind = 0
for _ in range(N):
    person = list(map(change_sign, input().rstrip().split()))
    person.append(ind % LINE_NUM)
    if ind == DEKA:
        person.append("DEKA")
    LINES[ind % LINE_NUM].append(person)
    ind += 1

HEADS = []
for line in LINES:
    if len(line) != 0:
        heapq.heappush(HEADS, line.popleft())

cnt = 0
try:
    while True:
        _, _, line_num = heapq.heappop(HEADS)
        cnt += 1

        if len(LINES[line_num]) != 0:
            heapq.heappush(HEADS, LINES[line_num].popleft())

except:
    print(cnt)
