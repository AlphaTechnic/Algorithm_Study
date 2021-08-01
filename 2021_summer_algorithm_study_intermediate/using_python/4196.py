"""
input :
1
3 2
1 2
2 3

output :
1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


def dfs(s):
    global NODE_NUM; global SCC_NUM
    NODE_NUM += 1
    dfn[s] = low[s] = NODE_NUM
    st.append(s)

    for nxt in graph[s]:
        if dfn[nxt] == 0:  # 처음 방문. 즉, tree edge를 타고 방문
            dfs(nxt)
            low[s] = min(low[s], low[nxt])
        else:
            if finished[nxt]: continue
            low[s] = min(low[s], dfn[nxt])

    if dfn[s] == low[s]:
        SCC_NUM += 1
        while True:
            node = st.pop()
            finished[node] = True
            scc[node] = SCC_NUM

            if node == s: break


def gen_indeg(group):
    for cur in group:
        for nxt in graph[cur]:
            if scc[cur] != scc[nxt]:
                indeg[scc[nxt]] += 1


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().rstrip().split())
        graph = [[] for _ in range(V + 1)]
        for i in range(E):
            a, b = map(int, input().rstrip().split())
            graph[a].append(b)

        SCC_NUM = 0
        NODE_NUM = 0
        dfn = [0 for _ in range(V + 1)]
        low = [0 for _ in range(V + 1)]
        finished = [False for _ in range(V + 1)]
        scc = [0 for _ in range(V + 1)]
        st = []
        for i in range(1, V + 1):
            # cross edge를 무시하기 위한 용도. pop을 한 바 있으면 finished된 것으로 처리
            if finished[i]: continue
            dfs(i)

        # SCC 결과 생성
        res = [[] for _ in range(V + 1)]
        for i in range(1, V + 1):
            res[scc[i]].append(i)
        res.sort()

        # SCC 단위로 하나의 노드처럼 묶어 indeg를 체크
        indeg = [0 for _ in range(SCC_NUM + 1)]
        for group in res:
            if len(group) == 0: continue
            gen_indeg(group)

        cnt = 0
        for i in range(1, SCC_NUM + 1):
            if indeg[i] == 0:
               cnt += 1
        print(cnt)
