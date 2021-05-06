"""
input :
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

output :
1
2
2
0
1
2
-1
0
1
-1
0
3
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

queue = deque([])
N = int(input())
for _ in range(N):
    instruction = input().split()
    if instruction[0] == 'push':
        queue.append(int(instruction[1]))
    elif instruction[0] == 'front':
        if len(queue) != 0:
            print(queue[0])
        else:
            print(-1)
    elif instruction[0] == 'back':
        if len(queue) != 0:
            print(queue[-1])
        else:
            print(-1)
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif instruction[0] == 'pop':
        if len(queue) != 0:
            print(queue.popleft())
        else:
            print(-1)
