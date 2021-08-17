"""
input :
21 6 12
1 9
1 10
10 12
2 13
13 11
11 12
3 8
8 7
8 12
5 19
5 14
14 12
6 20
6 21
20 15
15 12
4 18
4 17
17 16
16 12

output :
16
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(R):
    que = deque()
    que.append(R)
    visited[R] = 1

    while que:
        cur = que.popleft()
        for chd in graph[cur]:
            if visited[chd]: continue

            visited[chd] = visited[cur] + 1
            if 1 <= chd <= S:
                res.append(visited[chd] - 1)
                if len(res) == 2:
                    return

            que.append(chd)
    return


if __name__ == "__main__":
    V, S, R = map(int, input().rstrip().split())
    graph = dict()
    for i in range(1, V + 1):
        graph[i] = list()

    for _ in range(V - 1):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    res = list()
    visited = [0 for _ in range(V + 1)]
    bfs(R)
    print(V - sum(res) - 1)
