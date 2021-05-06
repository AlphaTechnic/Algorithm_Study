"""
input :
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

output :
2
1
2
0
2
1
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

N = int(input())
deq = deque([])
for _ in range(N):
    instruction = input().split()
    if instruction[0] == 'push_back':
        deq.append(int(instruction[1]))
    elif instruction[0] == 'push_front':
        deq.appendleft(int(instruction[1]))
    elif instruction[0] == 'front':
        if len(deq) != 0:
            print(deq[0])
        else:
            print(-1)
    elif instruction[0] == 'back':
        if len(deq) != 0:
            print(deq[-1])
        else:
            print(-1)
    elif instruction[0] == 'size':
        print(len(deq))
    elif instruction[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif instruction[0] == 'pop_back':
        if len(deq) != 0:
            print(deq.pop())
        else:
            print(-1)
    elif instruction[0] == 'pop_front':
        if len(deq) != 0:
            print(deq.popleft())
        else:
            print(-1)
