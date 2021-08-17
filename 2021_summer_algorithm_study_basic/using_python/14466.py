"""
input :
3 3 3
2 2 2 3
3 3 3 2
3 3 2 3
3 3
2 2
2 3

output :
2
"""
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def dfs(cy, cx):
    global r_cpy, c_cpy
    visited[cy][cx] = True
    if (cy, cx) != (r_cpy, c_cpy) and (cy, cx) in MOWS:
        ANS_SET.add((r_cpy, c_cpy, cy, cx))

    for dy, dx in move:
        ny, nx = cy + dy, cx + dx
        if not (1 <= ny <= N and 1 <= nx <= N): continue
        if (cy, cx, ny, nx) in WALL_SET: continue
        if visited[ny][nx]: continue

        dfs(ny, nx)


if __name__ == "__main__":
    N, K, R = map(int, input().rstrip().split())
    WALL_SET = set()
    MOWS = set()
    ANS_SET = set()
    for _ in range(R):
        a, b, c, d = map(int, input().rstrip().split())
        WALL_SET.add((a, b, c, d))
        WALL_SET.add((c, d, a, b))
    for _ in range(K):
        y, x = map(int, input().rstrip().split())
        MOWS.add((y, x))

    for r, c in MOWS:
        visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
        r_cpy, c_cpy = r, c
        dfs(r, c)

    tot = len(ANS_SET) // 2
    print((K * (K - 1)) // 2 - tot)
