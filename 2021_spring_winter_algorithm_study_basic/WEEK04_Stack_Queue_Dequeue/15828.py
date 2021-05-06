"""
input :
5
1
2
0
3
4
0
5
6
0
0
-1

output :
5 6
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

SIZE = int(input())
que = deque()
while True:
    num = int(input())
    if num == -1:
        break

    if num == 0:
        que.popleft()
    else:
        if len(que) == SIZE:
            pass
        else:
            que.append(num)

if len(que) == 0:
    print("empty")
else:
    for num in que:
        print(num, end=' ')
