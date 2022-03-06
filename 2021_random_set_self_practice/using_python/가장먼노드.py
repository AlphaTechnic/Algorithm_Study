from collections import defaultdict
from collections import deque

graph = defaultdict(list)


def bfs(start, vertex_num):
    max_depth = 0

    visited = [0 for _ in range(vertex_num + 1)]
    que = deque()
    visited[start] = 1
    que.append(start)
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if visited[nxt]:
                continue

            visited[nxt] = visited[cur] + 1
            max_depth = max(max_depth, visited[nxt])
            que.append(nxt)
    return max_depth, visited


def solution(n, edge):
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    max_depth, depths = bfs(start=1, vertex_num=n)

    return len(list(filter(lambda dep: dep == max_depth, depths)))


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
