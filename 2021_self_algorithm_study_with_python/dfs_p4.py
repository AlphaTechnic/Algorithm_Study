"""
특정하게 지정한 학생보다 성적이 높은 학생들을 조회하거나
특정하게 지정한 학생보다 성적이 낮은 학생들을 조회하고자 한다면,
# 로 표시한 주석문을 활용한다.
count만 올리는 방식에서 리스트에 학생을 기록해준다.

정확한 순위
input :
6 6
1 5
3 4
4 2
4 6
5 2
5 4
output :
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

V, E = map(int, input().split())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)

# reachable_to_x = [[] for _ in range(V + 1)]
# x_can_go = [[] for _ in range(V + 1)]
num_of_reachable_to_x = [0 for _ in range(V+1)]
num_of_node_x_can_go = [0 for _ in range (V+1)]

visited = [False for _ in range(V + 1)]



def dfs(start, cur):
    if len(graph[cur]) == 0:
        if not visited[cur]:
            # x_can_go[start].append(cur)
            # reachable_to_x[cur].append(start)
            num_of_node_x_can_go[start] += 1
            num_of_reachable_to_x[cur] += 1
        return

    for nxt in graph[cur]:
        if not visited[nxt]:
            # x_can_go[start].append(nxt)
            # reachable_to_x[nxt].append(start)
            num_of_node_x_can_go[start] += 1
            num_of_reachable_to_x[nxt] += 1
            visited[nxt] = True

        dfs(start, nxt)


for i in range(1, V + 1):
    visited = [False for _ in range(V + 1)]
    visited[i] = True
    dfs(i, i)

cnt = 0
for x in range(1, V + 1):
    # if len(reachable_to_x[x]) + len(x_can_go[x]) == V - 1:
    if num_of_node_x_can_go[x] + num_of_reachable_to_x[x] == V - 1:
        cnt += 1

print(cnt)
