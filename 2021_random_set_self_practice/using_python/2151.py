"""
input :

output :

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
        cy_save, cx_save, cdir_save = cy, cx, cdir = que.popleft()
        dy, dx = DIR[cdir]
        while True:
            cy, cx = cy + dy, cx + dx
            if not (0 <= cy < R and 0 <= cx < C) or bd[cy][cx] == '*':
                break
            if bd[cy][cx] == '!':
                if not vis[cy][cx][cdir]:
                    que.append((cy, cx, cdir))
                    vis[cy][cx][cdir] = vis[cy_save][cx_save][cdir_save]
                if not vis[cy][cx][(cdir + 1) % 4]:
                    que.append((cy, cx, (cdir + 1) % 4))
                    vis[cy][cx][(cdir + 1) % 4] = vis[cy_save][cx_save][cdir_save] + 1
                if not vis[cy][cx][(cdir - 1) % 4]:
                    que.append((cy, cx, (cdir - 1) % 4))
                    vis[cy][cx][(cdir - 1) % 4] = vis[cy_save][cx_save][cdir_save] + 1
            elif bd[cy][cx] == '#':
                return vis[cy_save][cx_save][cdir_save] - 1


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
