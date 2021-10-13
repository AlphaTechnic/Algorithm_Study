"""
input :
2
16
1 14
8 5
10 16
5 9
4 6
8 4
4 10
1 13
6 15
10 11
6 7
10 2
16 3
8 1
16 12
16 7
5
2 3
3 4
3 1
1 5
3 5

output :
4
3
"""
import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
LOG = 14


def find_rt(par):
    rt = 1
    while par[rt][0] != -1:
        rt = par[rt][0]
    return rt


def bfs(rt):
    que = deque()
    dep = [0 for _ in range(V + 1)]
    que.append(rt)
    dep[rt] = 1
    while que:
        cur = que.popleft()
        for nxt in grp[cur]:
            que.append(nxt)
            dep[nxt] = dep[cur] + 1
    return dep


def set_par(par):
    for num in range(1, LOG):
        for nd in range(1, V + 1):
            par[nd][num] = par[par[nd][num - 1]][num - 1]


def LCA(a, b):
    # 더 깊이 있는 놈을 항상 a로 지정
    if dep[a] < dep[b]:
        a, b = b, a

    # 깊이 있는 a를 b 깊이까지 끌어올림
    for i in range(LOG - 1, -1, -1):
        if (dep[a] - dep[b]) & (1 << i) == (1 << i):
            a = par[a][i]

    # 만약, a가 노드 b에 도달을 해버렸다면 return
    if a == b: return a

    # a와 b가 동시에 위로 jump jump
    for i in range(LOG - 1, -1, -1):
        if par[a][i] != par[b][i]:
            a = par[a][i]
            b = par[b][i]

    return par[a][0]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        V = int(input())

        par = [[-1 for _ in range(LOG)] for _ in range(V + 1)]
        grp = defaultdict(list)
        for _ in range(V - 1):
            a, b = map(int, input().rstrip().split())
            par[b][0] = a
            grp[a].append(b)

        # find root
        # set depth by bfs
        # set parents by dp
        rt = find_rt(par)
        dep = bfs(rt)
        set_par(par)

        a, b = map(int, input().rstrip().split())
        print(LCA(a, b))
