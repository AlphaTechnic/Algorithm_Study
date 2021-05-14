"""
input :
7
6
1 2
2 3
1 5
5 2
5 6
4 7

output :
4
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(s):
    cnt = 0
    st = []
    st.append(s)
    visited[s] = True

    while len(st) != 0:
        cur_node = st.pop()
        if not visited[cur_node]:
            visited[cur_node] = True
            cnt += 1

        for nxt_node in graph[cur_node]:
            if not visited[nxt_node]:
                st.append(nxt_node)

    return cnt


V = int(input().rstrip())
E = int(input().rstrip())

graph = ['_'] + [[] for _ in range(V)]
visited = [False for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(1))
