"""
input :
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 1 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

output :
1
3 2
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

DIR = ((-1, 1), (0, 1), (1, 1), (1, 0))


def chk(cy, cx, i):
    global R, C
    fr = bd[r][c]

    dy, dx = DIR[i]
    ny, nx = cy + dy, cx + dx
    for _ in range(4):
        if not (0 <= ny < R and 0 <= nx < C): return 0
        if bd[ny][nx] != fr: return 0
        ny, nx = ny + dy, nx + dx

    # 6목 방지
    y1, x1 = cy - dy, cx - dx
    if (0 <= y1 < R and 0 <= x1 < C) and bd[y1][x1] == fr:
        return 0
    y2, x2 = ny, nx
    if (0 <= y2 < R and 0 <= x2 < C) and bd[y2][x2] == fr:
        return 0
    return fr


if __name__ == "__main__":
    bd = [list(map(int, input().rstrip().split())) for _ in range(19)]
    R = len(bd)
    C = len(bd[0])

    for r in range(R):
        for c in range(C):
            for i in range(4):
                res = chk(r, c, i)
                if res != 0:
                    print(res)
                    print(r + 1, c + 1)
                    exit(0)
    print(0)
