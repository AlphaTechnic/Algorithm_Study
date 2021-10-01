"""
input :
7 9
1 4
4 5
5 1
1 6
6 7
2 7
7 3
3 7
7 2

output :
3
1 4 5 -1
2 3 7 -1
6 -1
"""
import sys
from collections import defaultdict
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

g_SCC_NUM = 0
g_nd_num = 0
g_st = []


def dfs(rt):
    global g_SCC_NUM, g_nd_num
    g_nd_num += 1
    dfn[rt] = low[rt] = g_nd_num
    g_st.append(rt)

    for nxt in graph[rt]:
        if dfn[nxt] == 0:  # 처음 방문
            dfs(nxt)
            low[rt] = min(low[rt], low[nxt])
        else:  # 쭉 타고 최상단 touch
            if fin[nxt]: continue

            low[rt] = min(low[rt], dfn[nxt])

    if dfn[rt] == low[rt]:  # 본인이 대표면, SCC_grp 창설
        g_SCC_NUM += 1
        while True:
            nd = g_st.pop()
            fin[nd] = True
            scc[nd] = g_SCC_NUM
            ans[g_SCC_NUM].append(nd)
            if nd == rt:
                break


def print_grp(grp):
    grp.sort()
    for mem in grp:
        print(mem, end=' ')
    print(-1)


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)

    dfn = [0 for _ in range(V + 1)]
    low = [0 for _ in range(V + 1)]
    fin = [False for _ in range(V + 1)]
    scc = [0 for _ in range(V + 1)]
    ans = [[] for _ in range(V + 1)]
    for i in range(1, V + 1):
        if fin[i]: continue
        dfs(i)

    print(g_SCC_NUM)
    ans.sort(key=lambda x: min(x) if len(x) != 0 else 0)
    for grp in ans:
        if len(grp) == 0: continue

        print_grp(grp)
