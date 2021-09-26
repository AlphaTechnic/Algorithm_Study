"""
input :
3
2 2 2
4 4 4
8 8 8

output :
16
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def mrg_line(line, t):
    global g_mxv
    L = len(line)
    nl = deque()

    if t == 'l':
        line.reverse()

    zcnt = 0
    tmp = deque()
    for i in range(L - 1, -1, -1):
        if line[i] == 0:
            zcnt += 1
            continue

        if len(tmp) >= 1 and tmp[0] == line[i]:
            a = tmp.popleft()
            tmp.appendleft(2 * a)
            nl = tmp + nl
            tmp.clear()
            zcnt += 1
            g_mxv = max(g_mxv, 2 * a)
        else:
            tmp.appendleft(line[i])
            g_mxv = max(g_mxv, line[i])
    nl = tmp + nl

    if t == 'r':
        nl = [0 for _ in range(zcnt)] + list(nl)
        return nl
    elif t == 'l':
        nl.reverse()
        nl = list(nl) + [0 for _ in range(zcnt)]
        return nl


def mov(bd, mt):
    L = len(bd)
    nbd = [[0 for _ in range(L)] for _ in range(L)]
    if mt == 0:
        for r in range(L):
            nl = mrg_line(bd[r], 'r')
            for c in range(L):
                nbd[r][c] = nl[c]
    elif mt == 1:
        for c in range(L):
            ol = [bd[r][c] for r in range(L)]
            nl = mrg_line(ol, 'r')
            for r in range(L):
                nbd[r][c] = nl[r]
    elif mt == 2:
        for r in range(L):
            nl = mrg_line(bd[r], 'l')
            for c in range(L):
                nbd[r][c] = nl[c]
    elif mt == 3:
        for c in range(L):
            ol = [bd[r][c] for r in range(L)]
            nl = mrg_line(ol, 'l')
            for r in range(L):
                nbd[r][c] = nl[r]
    return nbd


def find_mxv(bd):
    global N
    mxv = -1
    for r in range(N):
        for c in range(N):
            if bd[r][c] > mxv:
                mxv = bd[r][c]
    return mxv


if __name__ == "__main__":
    N = int(input())
    bds = []
    bd = [list(map(int, (input().rstrip().split()))) for _ in range(N)]
    bds.append(bd)

    g_mxv = -1
    for i in range(5):
        for j in range(4 ** i):
            bd = bds.pop(0)
            for mv_type in range(4):
                nbd = mov(bd, mv_type)
                if i != 4:  # 마지막탐색은 bds에 넣을 필요가 없다.
                    bds.append(nbd)

    print(g_mxv)
