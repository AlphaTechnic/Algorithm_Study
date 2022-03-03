import sys
from collections import deque
from collections import defaultdict

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(graph, V, start):
    visited = [0 for _ in range(V + 1)]
    que = deque()
    visited[start] = 1
    que.append(start)

    cnt = 0
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = visited[cur] + 1
                if visited[nxt] <= 3:
                    cnt += 1
                    que.append(nxt)

    return cnt


if __name__ == "__main__":
    V = int(input())
    E = int(input())

    graph = defaultdict(list)
    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = bfs(graph, V, 1)
    print(ans)
