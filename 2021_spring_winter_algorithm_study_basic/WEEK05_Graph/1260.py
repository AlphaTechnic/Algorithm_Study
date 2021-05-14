"""
input :
5 5 3
5 4
5 2
1 2
3 4
3 1

output :
3 1 2 5 4
3 1 4 2 5
"""

import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dfs(s):
    st = []
    st.append(s)
    visited_dfs[s] = True
    print(s, end=" ")

    graph[s].sort(reverse=True)

    while len(st) != 0:
        cur_node = st.pop()
        if not visited_dfs[cur_node]:
            visited_dfs[cur_node] = True
            print(cur_node, end=" ")
            graph[cur_node].sort(reverse=True)

        for nxt_node in graph[cur_node]:
            if not visited_dfs[nxt_node]:
                st.append(nxt_node)


def bfs(s):
    que = deque()
    que.append(s)
    visited_bfs[s] = True
    print(s, end=" ")

    graph[s].sort()

    while len(que) != 0:
        cur_node = que.popleft()
        if not visited_bfs[cur_node]:
            visited_bfs[cur_node] = True
            print(cur_node, end=" ")
            graph[cur_node].sort()

        for nxt_node in graph[cur_node]:
            if not visited_bfs[nxt_node]:
                que.append(nxt_node)


V, E, S = map(int, input().rstrip().split())

graph = ['_'] + [[] for _ in range(V)]
visited_dfs = [False for _ in range(V + 1)]
visited_bfs = [False for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(S)
print()
bfs(S)
