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
            graph_inv = [[] for _ in range(V + 1)]
            for i in range(0, 2 * E, 2):
                graph[nodes[i]].append(nodes[i + 1])
                graph_inv[nodes[i + 1]].append(nodes[i])

            # stack에 넣는 코사라주 dfs1()
            visited = [False for _ in range(V + 1)]
            st = []
            for i in range(1, V + 1):
                if visited[i]: continue

                dfs1(i)

            # stack에서 빼는 코사라주 dfs2()
            scc = [0 for _ in range(V + 1)]
            SCC_NUM = 0
            while len(st) != 0:
                cur = st.pop()
                if scc[cur] != 0: continue

                SCC_NUM += 1
                dfs2(cur)

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