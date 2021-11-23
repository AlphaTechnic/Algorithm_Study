"""
input :
4 3
1 3
2 3
4 2

output :
0 1
1 1
3 0
0 2
"""
import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

par_num = 0
chd_num = 0


def dfs1(cur):
    global par_num
    vis[cur] = True
    par_num += 1
    if not graph_par[cur]:
        return

    for nxt in graph_par[cur]:
        if vis[nxt]: continue
        dfs1(nxt)
    return


def dfs2(cur):
    global chd_num
    vis[cur] = True
    chd_num += 1
    if not graph_chd[cur]:
        return

    for nxt in graph_chd[cur]:
        if vis[nxt]: continue
        dfs2(nxt)
    return


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph_chd = defaultdict(list)
    graph_par = defaultdict(list)
    chk = [[False for _ in range(V + 1)] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        if chk[a][b]:
            continue
        else:
            chk[a][b] = True
            chk[b][a] = True
        graph_chd[a].append(b)
        graph_par[b].append(a)

    print(graph_chd)

    for i in range(1, V + 1):
        vis = [False for _ in range(V + 1)]
        par_num = 0
        dfs1(i)
        print(par_num - 1, end=' ')

        vis = [False for _ in range(V + 1)]
        chd_num = 0
        dfs2(i)
        print(chd_num - 1)
