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
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs1(s):
    visited[s] = True
    for nxt in graph[s]:
        if visited[nxt]: continue

        dfs1(nxt)

    st.append(s)


def dfs2(s):
    scc[s] = SCC_NUM
    for nxt in graph_inv[s]:
        if scc[nxt] != 0: continue

        dfs2(nxt)


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = [[] for _ in range(V + 1)]
    graph_inv = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph_inv[b].append(a)

    visited = [False for _ in range(V + 1)]
    st = []
    for i in range(1, V + 1):
        if visited[i]: continue

        dfs1(i)

    scc = [0 for _ in range(V + 1)]
    SCC_NUM = 0
    while len(st) != 0:
        p = st.pop()
        if scc[p] != 0: continue

        SCC_NUM += 1
        dfs2(p)

    res = [[] for _ in range(V + 1)]
    for i in range(1, V + 1):
        res[scc[i]].append(i)
    res.sort()

    print(SCC_NUM)
    for group in res:
        if group == []: continue
        for node in group:
            print(node, end=' ')
        print(-1)
