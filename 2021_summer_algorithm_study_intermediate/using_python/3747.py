"""
input :
3 3  +1 +2  -1 +2  -1 -3
2 3  -1 +2  -1 -2  +1 -2
2 4  -1 +2  -1 -2  +1 -2  +1 +2
2 8  +1 +2  +2 +1  +1 -2  +1 -2  -2 +1  -1 +1  -2 -2  +1 -1

output :
1 1 0 1
"""
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline


def dfs(s_node):
    global SCC_NUM; global NODE_NUM;
    NODE_NUM += 1
    dfn[s_node] = low[s_node] = NODE_NUM
    ST.append(s_node)

    for nxt in graph[s_node]:
        if dfn[nxt] == 0:  # 첫 방문
            dfs(nxt)
            low[s_node] = min(low[s_node], low[nxt])
        else:
            if finished[nxt]: continue
            low[s_node] = min(low[s_node], dfn[nxt])

    if dfn[s_node] == low[s_node]:
        SCC_NUM += 1
        while True:
            node = ST.pop()
            scc[node] = SCC_NUM
            finished[node] = True

            if node == s_node: break


def neg(a):
    if a <= N: return a + N
    else: return a - N


if __name__ == "__main__":
    lines = sys.stdin.readlines()
    data = []
    for line in lines:
        data += list(map(int, line.split()))

    ind = 0
    try:
        while True:
            N, M = data[ind], data[ind + 1]

            graph = [[] for _ in range(2 * N + 1)]
            for i in range(M):
                a, b = data[ind + 2 * i + 2], data[ind + 2 * i + 3]
                if a < 0: a = -a + N
                if b < 0: b = -b + N
                graph[neg(a)].append(b)
                graph[neg(b)].append(a)

            # 타잔 알고리즘
            NODE_NUM = SCC_NUM = 0
            finished = [False for _ in range(2 * N + 1)]
            scc = [0 for _ in range(2 * N + 1)]
            dfn = [0 for _ in range(2 * N + 1)]
            low = [0 for _ in range(2 * N + 1)]
            ST = []
            for i in range(1, 2 * N + 1):
                if finished[i]: continue
                dfs(i)

            for i in range(1, N + 1):
                if scc[i] == scc[i + N]:
                    print("0")
                    break
            else:
                print("1")

            ind += 2 * M + 2
    except:
        exit(0)