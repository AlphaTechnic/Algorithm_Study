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


def mk_nxt(nds, vis, seq):
    nd_nxts = [nd for nd in nds if not vis[nd]]
    seq_nxts = [seq.popleft() for _ in range(len(nd_nxts))]

    if set(nd_nxts) == set(seq_nxts):
        return seq_nxts
    else:
        return [-1]  # means failure


def bfs(s, seq):
    que = deque()
    vis = [False for _ in range(V + 1)]

    que.append(s)
    vis[s] = True
    if s != seq.popleft(): return False

    while que:
        cur = que.popleft()

        nxt_seq = mk_nxt(graph[cur], vis, seq)
        if nxt_seq == [-1]: return False

        for nxt in nxt_seq:
            if vis[nxt]: continue

            que.append(nxt)
            vis[nxt] = True

    return True


if __name__ == "__main__":
    V = int(input())
    graph = defaultdict(list)
    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)
    seq = deque(map(int, input().rstrip().split()))

    if bfs(1, seq):
        print(1)
    else:
        print(0)
