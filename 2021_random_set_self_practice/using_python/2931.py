"""
input :
3 7
.......
.M-.-Z.
.......

output :
2 4 -
"""
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


class Block:
    def __init__(self, shape, racc, dacc, lacc, uacc):
        self.shape = shape
        self.racc = racc
        self.dacc = dacc
        self.lacc = lacc
        self.uacc = uacc


def characterize(shape):
    if shape == '.':
        return shape, False, False, False, False
    if shape == '|':
        return shape, False, True, False, True
    if shape == '-':
        return shape, True, False, True, False
    if shape == '+':
        return shape, True, True, True, True
    if shape == '1':
        return shape, True, True, False, False
    if shape == '2':
        return shape, True, False, False, True
    if shape == '3':
        return shape, False, False, True, True
    if shape == '4':
        return shape, False, True, True, False
    if shape == 'M':
        return shape, True, True, True, True
    if shape == 'Z':
        return shape, True, True, True, True


def mk_nxts(cy, cx):
    nxts = []
    if bd[cy][cx].racc:
        nxts.append((cy, cx + 1))
    if bd[cy][cx].dacc:
        nxts.append((cy + 1, cx))
    if bd[cy][cx].lacc:
        nxts.append((cy, cx - 1))
    if bd[cy][cx].uacc:
        nxts.append((cy - 1, cx))
    return nxts


def leak(y, x):
    if bd[y][x].shape == 'M' or bd[y][x].shape == 'Z':
        return False

    if bd[y][x].racc and (x + 1 >= C or not bd[y][x + 1].lacc):
        return True
    if bd[y][x].dacc and (y + 1 >= R or not bd[y + 1][x].uacc):
        return True
    if bd[y][x].lacc and (x - 1 < 0 or not bd[y][x - 1].racc):
        return True
    if bd[y][x].uacc and (y - 1 < 0 or not bd[y - 1][x].dacc):
        return True
    return False


def bfs(My, Mx, Zy, Zx):
    global R, C
    que = deque()
    vis = [[False for _ in range(C)] for _ in range(R)]
    que.append((My, Mx))
    vis[My][Mx] = True
    while que:
        cy, cx = que.popleft()
        if (cy, cx) == (Zy, Zx):
            return True

        for ny, nx in mk_nxts(cy, cx):
            if not (0 <= ny < R and 0 <= nx < C): continue
            if vis[ny][nx]: continue
            if leak(ny, nx): return False

            if bd[cy][cx].shape == 'M' and bd[ny][nx].shape == 'Z':
                continue
            que.append((ny, nx))
            vis[ny][nx] = True
    return False


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    tmp = [list(input().rstrip()) for _ in range(R)]
    bd = []
    My = -1
    Mx = -1
    Zy = -1
    Zx = -1
    for rr in range(R):
        ln = []
        for cc in range(C):
            sh, r, d, l, u = characterize(tmp[rr][cc])
            if sh == 'M': My, Mx = rr, cc
            if sh == 'Z': Zy, Zx = rr, cc
            obj = Block(sh, r, d, l, u)
            ln.append(obj)
        bd.append(ln)

    SHAPE = ['|', '-', '+', '1', '2', '3', '4']
    for rr in range(R):
        for cc in range(C):
            for ii in range(7):
                if bd[rr][cc].shape != '.': continue

                sh, r, d, l, u = characterize(SHAPE[ii])
                obj = Block(sh, r, d, l, u)
                bd[rr][cc] = obj

                res = bfs(My, Mx, Zy, Zx)
                if res:
                    print(rr + 1, cc + 1, sh)
                    exit(0)

                bd[rr][cc] = Block('.', False, False, False, False)  # 원상복구
