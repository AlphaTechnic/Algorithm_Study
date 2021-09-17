"""
input :
10

output :
3
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def make_nxt(type, cur):
    if type == 0 and cur % 3 == 0:
        return cur // 3
    elif type == 1 and cur % 2 == 0:
        return cur // 2
    elif type == 2:
        return cur - 1
    return -1


def bfs(N):
    que = deque()
    visited = [0 for _ in range(N + 1)]
    visited[N] = 1
    que.append(N)
    while que:
        cur = que.popleft()

        for i in range(3):
            nxt = make_nxt(i, cur)
            if nxt == -1: continue
            if visited[nxt]: continue

            visited[nxt] = visited[cur] + 1
            que.append(nxt)
            if nxt == 1:
                return visited[1] - 1


if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(0)
        exit(0)

    print(bfs(N))
