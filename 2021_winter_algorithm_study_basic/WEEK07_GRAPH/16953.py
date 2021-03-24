import sys
sys.stdin = open("input.txt", "r")

from collections import deque

A, B = map(int, input().split())
ans = -1
que = deque([(A, 1)])
while que:
    i, cnt = que.popleft()
    if i == B:
        ans = cnt
        break

    mul2 = i * 2
    if mul2 <= B:
        que.append((mul2, cnt + 1))
    concat1 = i * 10 + 1
    if concat1 <= B:
        que.append((concat1, cnt + 1))

print(ans)