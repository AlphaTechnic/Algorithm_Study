"""
input :
14
push 1
push 2
top
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
top

output :
2
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
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
st = []
for _ in range(N):
    instruction = input().split()
    if instruction[0] == 'push':
        st.append(int(instruction[1]))
    elif instruction[0] == 'top':
        if len(st) != 0:
            print(st[-1])
        else:
            print(-1)
    elif instruction[0] == 'size':
        print(len(st))
    elif instruction[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif instruction[0] == 'pop':
        if len(st) != 0:
            print(st.pop())
        else:
            print(-1)
