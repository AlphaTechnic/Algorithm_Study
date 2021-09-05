"""
input :
7 392

output :
+*+
"""
import sys
import math
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_nxt(cur, op):
    if op == '*':
        return cur * cur
    elif op == '+':
        return cur + cur
    elif op == '-':
        return cur - cur
    else:
        if cur == 0:
            return -1
        else:
            return cur // cur


def bfs(N):
    global K
    que = deque()
    que.append(N)
    visited[N] = '_'
    while que:
        cur = que.popleft()
        for op in ['*', '+', '-', '/']:
            nxt = make_nxt(cur, op)
            if nxt == -1: continue
            if nxt > K: continue
            if nxt in visited: continue

            visited[nxt] = op
            que.append(nxt)
            if nxt == K:
                return True
    return False


def trace_back(cur, op):
    global N
    if op == '*':
        return int(math.sqrt(cur))
    elif op == '+':
        return cur // 2
    elif op == '-':
        return N
    elif op == '/':
        return N


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    if N == K:
        print(0)
        exit(0)

    visited = dict()
    if bfs(N):
        # print ans
        ans = deque()
        nxt = K
        while nxt != N:
            ans.appendleft(visited[nxt])
            nxt = trace_back(nxt, visited[nxt])

        for ele in ans:
            print(ele, end='')
    else:
        print(-1)
