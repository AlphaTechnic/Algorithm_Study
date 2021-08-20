"""
input :
3 3
1 2 2
3 1 3
2 3 2
1 3

output :
3
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 1000000001


def bfs(limit):
    global V, S, END;
    visited = [False for _ in range(V + 1)]
    que = deque()
    visited[S] = True
    que.append((0, S))
    while que:
        _, cur = que.popleft()
        for cap, nxt in graph[cur]:
            if visited[nxt]: continue
            if cap < limit: continue

            visited[nxt] = True
            que.append((cap, nxt))
            if nxt == END:
                return True
    return False


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(E):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((c, b))
        graph[b].append((c, a))
    S, END = map(int, input().rstrip().split())

    l = 1
    r = MAX
    mid_save = mid = (l + r) // 2
    while l <= r:
        if bfs(mid):
            mid_save = mid
            l = mid + 1
            mid = (l + r) // 2

        else:
            r = mid - 1
            mid = (l + r) // 2

    print(mid_save)
