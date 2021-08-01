"""
input :
3 3
1 3 2 3 3 1
2 1
1 2
0

output :
1 3
2
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


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


def sink_chk(group):
    group_scc = scc[group[0]]
    for node in group:
        for adj in graph[node]:
            if scc[adj] != group_scc:
                return False
    return True


if __name__ == "__main__":
    try:
        while True:
            V, E = map(int, input().rstrip().split())
            nodes = list(map(int, input().rstrip().split()))
            graph = [[] for _ in range(V + 1)]
            for i in range(0, 2 * E, 2):
                graph[nodes[i]].append(nodes[i + 1])

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

            # 하나의 scc 그룹이 outdegree가 없는지 체크하고, 없으면 ans에 넣음
            ans = []
            for group in res:
                if len(group) == 0: continue
                if not sink_chk(group): continue

                ans += group

            ans.sort()
            for node in ans:
                print(node, end=' ')
            print()
    except:
        pass
