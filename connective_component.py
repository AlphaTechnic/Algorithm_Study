import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10000)

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(cx, cy):
    if not -1 < cx < R: return False
    if not -1 < cy < C: return False

    if graph[cx][cy] == 0:
        graph[cx][cy] = 1
        for dx, dy in moves:
            nx, ny = cx + dx, cy + dy
            dfs(nx, ny)
        return True
    return False


R, C = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(map(int, input())))

ans = 0
visited = [[False for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        if dfs(i, j):
            ans += 1

print(ans)
