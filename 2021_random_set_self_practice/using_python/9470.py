"""
input :
1
1 7 8
1 3
2 3
6 4
3 4
3 5
6 7
5 7
4 7

output :
1 3
"""
import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def bfs(ss):
    que = deque(ss)
    mxv = 1

    for s in ss:
        vis[s] = 1
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if vis[nxt] > vis[cur]: continue

            if vis[nxt] < vis[cur]:  # 갱신
                vis[nxt] = vis[cur]
                que.append(nxt)
            elif vis[nxt] == vis[cur]:  # mxv again
                vis[nxt] = vis[cur] + 1
            mxv = max(mxv, vis[nxt])
    return mxv


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        Q, V, E = map(int, input().rstrip().split())
        graph = defaultdict(list)
        indegs = [0 for _ in range(V + 1)]
        for _ in range(E):
            a, b = map(int, input().rstrip().split())
            graph[a].append(b)
            indegs[b] += 1

        ss = [nd for nd, indeg in enumerate(indegs[1:], start=1) if indeg == 0]
        vis = [0 for _ in range(V + 1)]
        print(Q, bfs(ss))
