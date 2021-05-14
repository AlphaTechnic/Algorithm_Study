"""
input :
6 5
1 2
2 5
5 1
3 4
4 6

output :
2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(s):
    st = []
    st.append(s)
    visited[s] = True

    while len(st) != 0:
        cur_node = st.pop()
        if not visited[cur_node]: visited[cur_node] = True

        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                visited[nxt_node] = True
                st.append(nxt_node)


V, E = map(int, input().rstrip().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False for _ in range(V+1)]

cnt = 0
for i in range(1, V+1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)