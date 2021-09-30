"""
input :
......
......
......
......
......
......
......
......
.Y....
.YG...
RRYG..
RRYGG.

output :
3
"""
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def bfs(r, c, vis):
    grp = []

    sy, sx = r, c
    que = deque()
    que.append((r, c))
    vis[r][c] = True
    grp.append((r, c))
    while que:
        cy, cx = que.popleft()
        for dy, dx in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < 12 and 0 <= nx < 6): continue
            if vis[ny][nx]: continue
            if bd[ny][nx] != bd[sy][sx]: continue

            que.append((ny, nx))
            vis[ny][nx] = True
            grp.append((ny, nx))

    return grp


def to_dot(poses):
    for r, c in poses:
        bd[r][c] = '.'


def mk_dot():
    flag = False
    vis = [[False for _ in range(6)] for _ in range(12)]
    for r in range(12):
        for c in range(6):
            if bd[r][c] == '.': continue
            if vis[r][c]: continue

            poses = bfs(r, c, vis)
            if len(poses) >= 4:
                to_dot(poses)
                flag = True
    if flag:
        return True
    else:
        return False


def fall_down():
    for c in range(6):
        ind = 11
        for r in range(11, -1, -1):
            if bd[r][c] != '.':
                bd[ind][c] = bd[r][c]
                if ind != r:
                    bd[r][c] = '.'
                ind -= 1


if __name__ == "__main__":
    bd = [list(input().rstrip()) for _ in range(12)]

    cnt = 0
    while mk_dot():
        fall_down()
        cnt += 1
    print(cnt)
