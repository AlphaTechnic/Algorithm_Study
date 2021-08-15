"""
input :
4 4
1 2
2 3
3 1
3 4

output :
Cactus
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)


def dfs(p, mp):
    global NODE_NUM; global BCC_NUM;
    NODE_NUM += 1
    dfn[p] = low[p] = NODE_NUM

    for chd in graph[p]:
        if chd == mp: continue

        if dfn[chd] == 0:  # 처음 진입
            ST.append([p, chd])
            child[p] += 1
            dfs(chd, p)
            low[p] = min(low[p], low[chd])

            if dfn[p] <= low[chd]:
                if mp != -1:
                    AC[p] = True

                BCC_NUM += 1
                while True:
                    a, b = ST.pop()
                    BCC[BCC_NUM].append([a, b])
                    if [a, b] == [p, chd]: break

        elif dfn[chd] < dfn[p]:
            ST.append([p, chd])
            low[p] = min(low[p], dfn[chd])

    if mp == -1 and child[p] >= 2:
        AC[p] = True


def get_node_num(edges):
    chk_set = set()
    for edge in edges:
        chk_set.add(edge[0])
        chk_set.add(edge[1])

    return len(chk_set)


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
    AC = [False for _ in range(V + 1)]
    ST = list()
    NODE_NUM = 0
    BCC_NUM = 0
    for i in range(1, V + 1):
        if dfn[i]: continue

        dfs(i, -1)

    # < 선인장일 조건 >
    # 크기가 3 이상인 BCC이면, 간선개수 = 정점개수
    # 각 정점별로 크기가 3 이상인 BCC는 하나 이하로만 있어야함
    nd2bccnums = dict()
    for i in range(1, V + 1):
        nd2bccnums[i] = set()

    for b_num in range(1, BCC_NUM + 1):
        for edge in BCC[b_num]:
            nd2bccnums[edge[0]].add(b_num)
            nd2bccnums[edge[1]].add(b_num)

    for nd in nd2bccnums:
        cnt = 0
        for b_num in nd2bccnums[nd]:
            if len(BCC[b_num]) >= 3:
                cnt += 1
                if cnt > 1:  # 하나의 정점에 '크기3이상의BCC'가 여러개 걸려있으면 안된다. (많아야 1개)
                    print("Not cactus")
                    exit()
                if len(BCC[b_num]) != get_node_num(BCC[b_num]):  # '크기3이상의BCC'가 달려 있으려면, 필히 간선 개수 == 정점 개수 여야함
                    print("Not cactus")
                    exit()
    print("Cactus")
