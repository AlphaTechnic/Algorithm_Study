"""
input :
10 6 6
9 15 4 4 1 5 19 14 20 5
1 3
2 5
4 9
6 2
7 8
6 10

output :
57
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def bfs(s):
    tot = 0
    cnt = 0
    que = deque()

    visited[s] = True
    que.append(s)
    cnt += 1
    tot += node_val[s]
    while que:
        cur = que.popleft()
        for nxt in graph[cur]:
            if visited[nxt]: continue

            tot += node_val[nxt]
            cnt += 1
            que.append(nxt)
            visited[nxt] = True

    return tot, cnt


if __name__ == "__main__":
    V, E, K = map(int, input().rstrip().split())
    node_val = [0] + list(map(int, input().rstrip().split()))

    graph = dict()
    for i in range(V + 1):
        graph[i] = list()

    for _ in range(E):
        a, b = map(int, input().rstrip().split())
        graph[a].append(b)
        graph[b].append(a)

    P = []
    W = []
    visited = [False for _ in range(V + 1)]
    for i in range(1, V + 1):
        if visited[i]: continue

        val, w = bfs(i)
        P.append(val)
        W.append(w)

    # 냅색 문제를 풀이
    dp = [[0 for _ in range(3001)] for _ in range(len(P))]
    for i in range(len(P)):
        for j in range(3001):
            if W[i] < j:
                dp[i][j] = max(P[i] + dp[i - 1][j - W[i]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]

    print(dp[len(P) - 1][K])
