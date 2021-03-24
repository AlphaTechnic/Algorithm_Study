import sys
sys.stdin = open("input.txt", "r")

import collections
MAX = 301
INF = 987654321
input = sys.stdin.readline
K = int(input())

while K != 0:
    K -= 1
    ans = 0
    C = [[0 for _ in range(MAX)] for _ in range(MAX)]
    F = [[0 for _ in range(MAX)] for _ in range(MAX)]
    P = []
    V = [[] for _ in range(MAX)]

    N, M = map(int, input().split())
    for i in range(M):
        f, t, cost = map(int, input().split())
        C[f][t] += cost
        V[f].append(t)
        V[t].append(f)
        P.append([f, t])

    while True:
        flow = INF
        D = [-1 for _ in range(N + 1)]
        Q = collections.deque()
        Q.append(1)

        while len(Q) != 0:
            x = Q[0]
            Q.popleft()
            for y in V[x]:
                if C[x][y] - F[x][y] > 0 and D[y] == -1:
                    Q.append(y)
                    D[y] = x
                    if y == N:
                        break

        if D[N] == -1:
            break

        i = N
        while True:
            if i == 1:
                break
            flow = min(flow, C[D[i]][i] - F[D[i]][i])
            i = D[i]

        i = N
        while True:
            if i == 1:
                break
            F[D[i]][i] += flow
            F[i][D[i]] -= flow
            i = D[i]

    for i in range(len(P)):
        x = P[i][0]
        y = P[i][1]

        Q = collections.deque()
        D = [-1 for _ in range(N + 1)]
        Q.append(x)

        while len(Q) != 0 and D[y] == -1:
            cur = Q[0]
            Q.popleft()
            for nxt in V[cur]:
                if C[cur][nxt] - F[cur][nxt] > 0 and D[nxt] == -1:
                    Q.append(nxt)
                    D[nxt] = cur
                    if nxt == y:
                        break

        if D[y] == -1:
            ans += 1

    print(ans)