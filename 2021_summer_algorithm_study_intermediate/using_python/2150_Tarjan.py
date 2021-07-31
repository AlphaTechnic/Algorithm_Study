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


def dfs(s):
    global node_num
    global SCC_NUM
    node_num += 1
    dfn[s] = low[s] = node_num
    st.append(s)

    for nxt in graph[s]:
        if dfn[nxt] == 0:  # 처음 방문. 즉, tree edge
            dfs(nxt)
            low[s] = min(low[s], low[nxt])
        else:
            if finished[nxt]: continue

            low[s] = min(low[s], dfn[nxt])

    if dfn[s] == low[s]:
        SCC_NUM += 1
        tmp = []
        while True:
            nxt = st.pop()
            tmp.append(nxt)
            scc[nxt] = SCC_NUM
            finished[nxt] = True

            if nxt == s:
                break

        tmp.sort()
        ans.append(tmp)


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)

    SCC_NUM = 0
    node_num = 0
    dfn = [0 for _ in range(V + 1)]
    low = [0 for _ in range(V + 1)]
    finished = [False for _ in range(V + 1)]
    scc = [0 for _ in range(V + 1)]
    st = []
    ans = []
    for i in range(1, V + 1):
        if finished[i]: continue
        dfs(i)

    print(SCC_NUM)
    ans.sort()
    for scc in ans:
        for node in scc:
            print(node, end =' ')
        print(-1)