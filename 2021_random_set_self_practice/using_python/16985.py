"""
input :
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
1 1 1 1 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

output :
12
"""
import sys
from collections import deque
from itertools import permutations

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 10 ** 9
g_mnv = MAX


def rot(bd):
    nbd = [[0 for _ in range(5)] for _ in range(5)]
    for r in range(5):
        ol = bd[r]
        c = r
        for rr in range(4, -1, -1):
            nbd[rr][c] = ol[4 - rr]
    return nbd


def bfs(bds):
    if bds[0][0][0] == 0:
        return MAX

    que = deque()
    vis = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    vis[0][0][0] = 1
    que.append((0, 0, 0))
    while que:
        cz, cy, cx = que.popleft()
        for dz, dy, dx in [(0, 0, 1), (0, 1, 0), (0, 0, -1), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]:
            nz, ny, nx = cz + dz, cy + dy, cx + dx
            if not (0 <= nz < 5 and 0 <= ny < 5 and 0 <= nx < 5): continue
            if bds[nz][ny][nx] == 0: continue
            if vis[nz][ny][nx]: continue

            que.append((nz, ny, nx))
            vis[nz][ny][nx] = vis[cz][cy][cx] + 1
            if (nz, ny, nx) == (4, 4, 4):
                return vis[nz][ny][nx] - 1
    return MAX


def recur(bds, perm, N):
    global g_mnv
    if len(bds) == 5:
        g_mnv = min(g_mnv, bfs(bds))

        # pruning : 12를 봤다면 그보다 짧아질 수는 없다.
        if g_mnv == 12:
            print(12)
            exit(0)
        return

    bd = perm[N]
    for i in range(4):
        bd = rot(bd)
        bds.append(bd)
        recur(bds, perm, N + 1)
        bds.pop()


if __name__ == "__main__":
    bds = []
    for _ in range(5):
        bd = [list(map(int, input().rstrip().split())) for _ in range(5)]
        bds.append(bd)

    permus = list(permutations(bds, 5))
    for perm in permus:
        recur([], perm, 0)

    if g_mnv == MAX:
        print(-1)
    else:
        print(g_mnv)
