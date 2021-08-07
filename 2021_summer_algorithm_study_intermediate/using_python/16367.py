"""
input :
7 5
3 R 5 R 6 B
1 B 2 B 3 R
4 R 5 B 6 B
5 R 6 B 7 B
1 R 2 R 4 R

output :
BRRRBBB
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
    N, M = map(int, input().rstrip().split())
    graph = [[] for _ in range(2 * N + 1)]
    for _ in range(M):
        # R -> true, B -> false
        a, RB1, b, RB2, c, RB3 = list(input().rstrip().split())
        a, b, c = map(int, [a, b, c])
        if RB1 == 'B': a = a + N
        if RB2 == 'B': b = b + N
        if RB3 == 'B': c = c + N
        graph[neg(a)].append(b)
        graph[neg(b)].append(a)
        graph[neg(b)].append(c)
        graph[neg(c)].append(b)
        graph[neg(c)].append(a)
        graph[neg(a)].append(c)

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
            print(-1)
            exit(0)

    for i in range(1, N + 1):
        # scc 넘버가 크다? -> 위상 정렬 상 앞에 있다는 얘기 -> 해당 노드에 false를 박음
        if scc[i] > scc[i + N]:
            print('B', end='')
        else:
            print('R', end='')
