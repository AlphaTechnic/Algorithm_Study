"""
input :
4 3
1 2
-2 -3
2 4
2 4
1 2
1 -2
-1 2
-1 -2

output :
yes
no
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
    while True:
        try:
            N, M = map(int, input().rstrip().split())
            graph = [[] for _ in range(2 * N + 2)]
            for _ in range(M):
                a, b = map(int, input().rstrip().split())
                if a < 0: a = -a + N
                if b < 0: b = -b + N
                graph[neg(a)].append(b)
                graph[neg(b)].append(a)
            # x_1이 반드시 true여야 한다는 조건 : ~x1 -> x1 을 추가
            graph[neg(1)].append(1)

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
                    print("no")
                    break
            else:
                print("yes")

        except:
            exit(0)
