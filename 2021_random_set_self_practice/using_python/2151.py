"""
input :
5
***#*
*.!.*
*!.!*
*.!.*
*#***

output :
2
"""
from collections import deque
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

DIR = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs(sy, sx):
    que = deque()
    vis = [[[0 for _ in range(4)] for _ in range(C)] for _ in range(R)]
    for dir in range(4):
        que.append((sy, sx, dir))
        vis[sy][sx][dir] = 1
    while que:
        cy, cx, cdir = que.popleft()
        dy, dx = DIR[cdir]
        ny, nx = cy, cx
        while True:
            ny, nx = ny + dy, nx + dx
            if not (0 <= ny < R and 0 <= nx < C) or bd[ny][nx] == '*':
                break
            if bd[ny][nx] == '!':
                if not vis[ny][nx][cdir]:
                    que.append((ny, nx, cdir))
                    vis[ny][nx][cdir] = vis[cy][cx][cdir]
                if not vis[ny][nx][(cdir + 1) % 4]:
                    que.append((ny, nx, (cdir + 1) % 4))
                    vis[ny][nx][(cdir + 1) % 4] = vis[cy][cx][cdir] + 1
                if not vis[ny][nx][(cdir - 1) % 4]:
                    que.append((ny, nx, (cdir - 1) % 4))
                    vis[ny][nx][(cdir - 1) % 4] = vis[cy][cx][cdir] + 1
            elif bd[ny][nx] == '#':
                return vis[cy][cx][cdir] - 1


if __name__ == "__main__":
    R = C = int(input())
    bd = [list(input().rstrip()) for _ in range(R)]

    sy = sx = ey = ex = -1
    for r in range(R):
        for c in range(C):
            if bd[r][c] == '#':
                if sy == -1:
                    sy, sx = r, c
                    bd[sy][sx] = 'S'
                else:
                    ey, ex = r, c

    print(bfs(sy, sx))
