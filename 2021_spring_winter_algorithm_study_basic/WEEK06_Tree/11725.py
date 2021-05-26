"""
input :
7
1 6
6 3
3 5
4 1
2 4
4 7

output :
4
6
1
3
1
4
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [-1 for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
def dfs(S):
    st = []
    st.append(S)
    visited[S] = True

    while len(st) != 0:
        cur_node = st.pop()
        if not visited[cur_node]: visited[cur_node] = True

        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                parent[nxt_node] = cur_node
                st.append(nxt_node)


dfs(1)
for i in range(2, N + 1):
    print(parent[i])
