"""
input :
2 162

output :
5
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_nxt(i, cur):
    if i == 0:
        return cur * 2
    elif i == 1:
        return int(str(cur) + '1')


def bfs(s):
    global K
    que = deque()
    visited = dict()
    que.append(s)
    visited[s] = 1
    while que:
        cur = que.popleft()
        for i in range(2):
            nxt = make_nxt(i, cur)
            if nxt > K: continue
            if nxt in visited: continue

            visited[nxt] = visited[cur] + 1
            que.append(nxt)
            if nxt == K:
                return visited[nxt]
    return -1


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())

    res = bfs(N)
    if res != -1:
        print(res)
    else:
        print(-1)
