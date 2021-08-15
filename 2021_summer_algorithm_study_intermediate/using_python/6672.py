"""
input :
3 3
0 1
0 2
2 1
4 2
0 1
2 3
3 1
1 0
0 0

output :
1
2
2
"""
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline


def dfs(p, mp):
    global NODE_NUM; global BCC_NUM;
    NODE_NUM += 1
    dfn[p] = low[p] = NODE_NUM

    for chd in graph[p]:
        if chd == mp: continue

        if dfn[chd] == 0:
            ST.append([p, chd])
            child[p] += 1
            dfs(chd, p)
            low[p] = min(low[p], low[chd])

            #  p가 꽤 중요한 점(분절점)이라는 것을 알게됨
            if dfn[p] <= low[chd]:
                if mp != -1:
                    AC[p] += 1

                BCC_NUM += 1
                while True:
                    [a, b] = ST.pop()
                    BCC[BCC_NUM].append([a, b])
                    if [a, b] == [p, chd]: break

        # 조상까지 touch
        elif dfn[p] > dfn[chd]:
            low[p] = min(low[p], dfn[chd])
            ST.append([p, chd])

    if mp == -1 and child[p] >= 2:
        AC[p] += 1


if __name__ == "__main__":
    while True:
        V, E = map(int, input().rstrip().split())
        if [V, E] == [0, 0]: break
        if E == 0:
            print(V - 1)
            continue

        graph = dict()
        for i in range(V):
            graph[i] = list()

        for _ in range(E):
            a, b = map(int, input().rstrip().split())
            graph[a].append(b)
            graph[b].append(a)

        BCC = [[] for _ in range(V)]
        dfn = [0 for _ in range(V)]
        low = [0 for _ in range(V)]
        child = [0 for _ in range(V)]
        ST = list()
        AC = [0 for _ in range(V)]
        NODE_NUM = 0
        BCC_NUM = 0
        component_num = 0
        for i in range(V):
            if dfn[i]: continue

            dfs(i, -1)
            component_num += 1

        print(max(AC) + component_num)
