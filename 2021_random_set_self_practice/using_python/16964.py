"""
input :
4
1 2
1 3
2 4
1 2 3 4

output :
1
"""
import sys
from collections import defaultdict

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def dfs(cur):
    global ND_NUM
    ND_NUM += 1
    dfn[cur] = ND_NUM

    for nxt in graph[cur]:
        if dfn[nxt] != -1: continue

        dfs(nxt)


if __name__ == "__main__":
    V = int(input())
    graph = defaultdict(list)
    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    seq = list(map(int, input().rstrip().split()))
    dfn_expected = [-1 for _ in range(V + 1)]
    for i, nd in enumerate(seq):
        dfn_expected[nd] = i + 1

    for grp in graph.values():
        grp.sort(key=lambda x: dfn_expected[x])

    dfn = [-1 for _ in range(V + 1)]
    ND_NUM = 0
    dfs(1)

    if dfn != dfn_expected:
        print(0)
    else:
        print(1)
