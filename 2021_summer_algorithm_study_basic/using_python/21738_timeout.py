"""
input :
21 6 12
1 9
1 10
10 12
2 13
13 11
11 12
3 8
8 7
8 12
5 19
5 14
14 12
6 20
6 21
20 15
15 12
4 18
4 17
17 16
16 12

output :
16
"""
import sys
sys.setrecursionlimit(10 ** 8)
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gen_dfs_tree(p, mp):
    global S
    if 1 <= p <= S:
        return

    for chd in graph[p]:
        if chd == mp: continue
        dfs_tree[p].append(chd)
        gen_dfs_tree(chd, p)


def bfs(R):
    que = deque()
    que.append((R, 0))

    while que:
        cur, dep = que.popleft()

        for chd in graph[cur]:
            if 1 <= chd <= S:
                res.append(dep + 1)
                if len(res) == 2:
                    return

            que.append((chd, dep + 1))
    return


if __name__ == "__main__":
    V, S, R = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    dfs_tree = dict()
    for i in range(1, V + 1):
        dfs_tree[i] = list()
    gen_dfs_tree(R, -1)

    res = list()
    bfs(R)
    print(V - sum(res) - 1)
