import sys
sys.stdin = open("input.txt", "r")
MAX = 30

graph = [[0] for _ in range(MAX)]
C = [[0 for _ in range(MAX)] for _ in range(MAX)]
F = [[0 for _ in range(MAX)] for _ in range(MAX)]

input = sys.stdin.readline
N, M, K = map(int, input().split())

for i in range(1, N+1):
    line = list(map(int, input().split()))
    for j in line[1:]:
        graph[i].append(N+j)
        graph[N+j].append(i)
        C[i][N+j] = 1

for i in range(1, N+1):
    graph[0].append(i)
    graph[i].append(0)
    C[0][i] = 1

for i in range(N+1, N+M+1):
    graph[i].append(N+M+1)
    graph[N+M+1].append(i)
    C[i][N+M+1] = 1

graph[0].append(N+M+2)
graph[N+M+2].append(0)
C[0][N+M+2] = K
for i in range(1, N+1):
    graph[N+M+2].append(i)
    graph[i].append(N+M+2)
    C[N+M+2][i] = 1

ans = 0
while True:
    prev = [-1]*MAX
    Q = []
    Q.append(0)
    while len(Q) != 0 and prev[N + M + 1] == -1:
        cur = Q[0]
        Q.pop()
        for nxt in graph[cur]:
            if C[cur][nxt] - F[cur][nxt] > 0 and prev[nxt] == -1:
                Q.append(nxt)
                prev[nxt] = cur
                if nxt == N+M+1:
                    break

    if prev[N+M+1] == -1:
        break

    i = N + M + 1
    while True:
        if i == 0:
            break
        F[prev[i]][i] += 1
        F[i][prev[i]] -= 1
        i = prev[i]

    ans += 1

print(ans)