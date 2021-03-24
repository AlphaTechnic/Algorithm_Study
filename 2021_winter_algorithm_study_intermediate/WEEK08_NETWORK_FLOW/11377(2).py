import sys
sys.stdin = open("input.txt", "r")

sys.setrecursionlimit(2000)
MAX = 1002

vec = [[0] for _ in range(MAX*2)]


def dfs(cur):
    visited[cur] = True
    for v in vec[cur][1:]:
        if B[v] == -1 or visited[B[v]] is False and dfs(B[v]):
            B[v] = cur
            return True
    return False


input = sys.stdin.readline
N, M, K = map(int, input().split())
B = [-1 for _ in range(MAX)]

for i in range(N):
    line = list(map(int, input().split()))
    for num in line[1:]:
        vec[i].append(num)
        vec[N+i].append(num)

ans = 0
for i in range(N):
    visited = [False for _ in range(MAX * 2)]
    if dfs(i):
        ans += 1

sa = 0
for i in range(N, 2*N):
    visited = [False for _ in range(MAX * 2)]
    if dfs(i):
        sa += 1

print(ans + min(sa, K))
