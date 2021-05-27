"""
input :
6 1 1
1 2
2 3
2 4
3 5
5 6

output :
6
"""

import sys
sys.setrecursionlimit(10**7)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

V, START, D = map(int, input().rstrip().split())
graph = [[] for _ in range(V + 1)]
for _ in range(V - 1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

leaves = []
for i in range(1, V + 1):
    if i != START and len(graph[i]) == 1:
        leaves.append(i)

max_depths = [0 for _ in range(V + 1)]


def get_max_depth_by_dfs(cur):
    if len(graph[cur]) == 1 and cur != START:
        return 0

    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            max_depths[cur] = max(max_depths[cur], get_max_depth_by_dfs(nxt) + 1)

    return max_depths[cur]


visited = [False for _ in range(V + 1)]
visited[START] = True
get_max_depth_by_dfs(START)


cnt = 0
for i in range(1, V+1):
    if max_depths[i] >= D:
       cnt += 1

if cnt - 1 <= 0:
    print(0)
else:
    print(2 * (cnt-1))