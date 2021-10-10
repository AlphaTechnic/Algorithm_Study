"""
input :
6
1 2
2 3
3 4
4 5
4 6

output :
DUDUDUNGA
"""
import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def bfs(s):
    D = 0
    que = deque()
    vis = [False for _ in range(V + 1)]
    que.append(s)
    vis[s] = True
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if vis[nxt]: continue

            D += (deg[cur] - 1) * (deg[nxt] - 1)
            que.append(nxt)
            vis[nxt] = True
    return D


if __name__ == "__main__":
    V = int(input())
    graph = defaultdict(list)
    deg = [0 for _ in range(V + 1)]
    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        deg[a] += 1
        deg[b] += 1
        graph[a].append(b)
        graph[b].append(a)

    # G
    Gnum = 0
    for d in deg:
        if d >= 3:
            Gnum += (d * (d - 1) * (d - 2)) // 6

    # D
    rt = 1
    Dnum = bfs(rt)

    if Dnum > 3 * Gnum:
        print('D')
    elif Dnum < 3 * Gnum:
        print('G')
    else:
        print("DUDUDUNGA")
