"""
input :
7 7
1 4
4 5
5 1
1 6
6 7
2 7
7 3

output :
3
1 6 7
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def dfs(p, mp=-1):
    global NODE_NUM; global BCC_NUM;
    NODE_NUM += 1
    dfn[p] = low[p] = NODE_NUM
    for chd in graph[p]:
        if chd == mp: continue

        if not dfn[chd]:  # 처음 방문 Tree edge
            ST.append([p, chd])
            child[p] += 1  # 루트노드는 자식노드가 2개 이상일 때 단절점이다. 그 부분을 관리하기 위함.
            dfs(chd, p)
            low[p] = min(low[p], low[chd])

            # BCC 감지!!!
            if dfn[p] <= low[chd]:
                if mp != -1: CUT_ND[p] = True  # 루트노드 예외를 제외하고, 처음 BCC를 감지하게 되는 이 순간이 단절점

                BCC_NUM += 1
                while True:
                    [a, b] = ST.pop()
                    BCC[BCC_NUM].append([a, b])
                    if [a, b] == [p, chd]: break

        elif dfn[p] > dfn[chd]:
            # 간선의 중복방문을 막기위해 자식에서 조상으로 가는 경우만 관찰
            # 즉 여기선 chd가 chd가 아님(조상임)
            low[p] = min(low[p], dfn[chd])
            ST.append([p, chd])

    if mp == -1 and child[p] >= 2:
        CUT_ND[p] = True


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    BCC = [[] for _ in range(V + 1)]
    dfn = [0 for _ in range(V + 1)]
    low = [0 for _ in range(V + 1)]
    child = [0 for _ in range(V + 1)]
    CUT_ND = [False for _ in range(V + 1)]
    ST = []
    NODE_NUM = 0
    BCC_NUM = 0
    for i in range(1, V + 1):
        if dfn[i]: continue

        dfs(i, -1)

    #  print ans
    ans = []
    for i, is_true in enumerate(CUT_ND):
        if is_true:
            ans.append(i)
    ans.sort()

    print(len(ans))
    for nd in ans:
        print(nd, end=' ')
