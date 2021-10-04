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
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def bfs(s):
    global ND_NUM
    que = deque()

    que.append(s)
    ND_NUM += 1
    bfn[s] = ND_NUM
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if bfn[nxt] != -1: continue

            que.append(nxt)
            ND_NUM += 1
            bfn[nxt] = ND_NUM


if __name__ == "__main__":
    V = int(input())
    graph = defaultdict(list)
    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    seq = deque(map(int, input().rstrip().split()))
    bfn_expected = [-1 for _ in range(V + 1)]
    for i, nd in enumerate(seq):
        bfn_expected[nd] = i + 1

    for grp in graph.values():
        grp.sort(key=lambda x: bfn_expected[x])

    bfn = [-1 for _ in range(V + 1)]
    ND_NUM = 0
    bfs(1)

    if bfn == bfn_expected:
        print(1)
    else:
        print(0)
