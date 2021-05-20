"""
input :
5
-1 0 0 1 1
2

output :
2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
parents = list(map(int, input().rstrip().split()))
tar = int(input())

graph = [[] for _ in range(N)]
for i in range(N):
    parent = parents[i]
    if parent != -1:
        graph[parent].append(i)
    else:
        root = i


def dfs_for_num_of_leaves(S):
    cnt = 0

    st = []
    st.append(S)
    visited[S] = True
    # 말단노드가 root라면, leaf의 갯수는 1개
    if len(graph[S]) == 0: return 1

    while len(st) != 0:
        parent_node = st.pop()
        if not visited[parent_node]: visited[parent_node] = True

        for child_node in graph[parent_node]:
            if visited[child_node]: continue

            visited[child_node] = True
            if len(graph[child_node]) == 0:
                cnt += 1
            st.append(child_node)

    return cnt


visited = [False for _ in range(N)]
original = dfs_for_num_of_leaves(root)

visited = [False for _ in range(N)]
elimi = dfs_for_num_of_leaves(tar)

# 지우려는 노드의 부모노드가 해당 노드를 유일한 자식노드로 갖는 경우
if len(graph[parents[tar]]) == 1:
    elimi -= 1

print(original - elimi)