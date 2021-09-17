"""
input :
4 5 1
1 2
1 3
1 4
2 4
3 4

output:
1 2 4 3
1 2 3 4
"""
import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(s):
    visited_dfs[s] = True
    dfs_path.append(s)

    for nxt in graph[s]:
        if visited_dfs[nxt]: continue

        dfs(nxt)


def bfs(s):
    ans = list()
    ans.append(s)

    que = deque()
    visited_bfs = [False for _ in range(V + 1)]
    que.append(s)
    visited_bfs[s] = True
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if visited_bfs[nxt]: continue

            que.append(nxt)
            visited_bfs[nxt] = True
            ans.append(nxt)

    return ans


if __name__ == "__main__":
    V, E, S = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    chk = set()
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        if (a, b) in chk: continue
        graph[a].append(b)
        graph[b].append(a)
        chk.add((a, b))
        chk.add((b, a))

    for i in range(1, V + 1):
        graph[i].sort()

    dfs_path = list()
    visited_dfs = [False for _ in range(V + 1)]
    dfs(S)
    for nd in dfs_path:
        print(nd, end=' ')
    print()

    bfs_path = bfs(S)
    for nd in bfs_path:
        print(nd, end=' ')
