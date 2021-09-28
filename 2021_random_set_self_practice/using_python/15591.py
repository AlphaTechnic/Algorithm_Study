"""
input :
4 3
1 2 3
2 3 2
2 4 4
1 2
4 1
3 1

output :
3
0
2
"""
import sys
from collections import deque
from collections import defaultdict

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
MAX = 10 ** 9


def cnt_nd(vis, v):
    cnt = 0
    for nd, c in enumerate(vis):
        if nd == v: continue

        if c != MAX:
            cnt += 1
    return cnt


def bfs(k, v):
    global V
    que = deque()
    vis = [MAX for _ in range(V + 1)]
    que.append((v, '_'))
    vis[v] = MAX - 1
    while que:
        cv, cc = que.popleft()
        for nv, nc in graph[cv]:
            if nc < k: continue
            if vis[nv] != MAX: continue

            que.append((nv, nc))
            vis[nv] = min(vis[cv], nc)

    return cnt_nd(vis, v)


if __name__ == "__main__":
    V, Q = map(int, input().rstrip().split())
    graph = defaultdict(list)
    for _ in range(V - 1):
        a, b, c = map(int, input().rstrip().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    for _ in range(Q):
        k, v = map(int, input().rstrip().split())
        print(bfs(k, v))
