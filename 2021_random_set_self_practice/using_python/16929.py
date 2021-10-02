"""
input :
3 4
AAAA
ABCA
AAAA

output :
Yes
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
g_flag = False
g_sy, g_sx = -1, -1


def dfs(py, px, cy, cx):
    global R, C, g_flag
    vis[cy][cx] = True
    for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
        ny, nx = cy + dy, cx + dx
        if not (0 <= ny < R and 0 <= nx < C): continue
        if (ny, nx) == (py, px): continue
        if bd[ny][nx] != bd[g_sy][g_sx]: continue

        if vis[ny][nx]:
            g_flag = True
            return
        vis[ny][nx] = True
        dfs(cy, cx, ny, nx)


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    bd = [list(input().rstrip()) for _ in range(R)]

    vis = [[False for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if vis[r][c]: continue

            g_sy, g_sx = r, c
            dfs(-1, -1, r, c)
            if g_flag:
                print("Yes")
                exit(0)
    print("No")
