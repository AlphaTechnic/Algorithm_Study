"""
input :
6 3
0000000000
0000000300
0054000300
1054502230
2211122220
1111111223

output :
0000000000
0000000000
0000000000
0000000000
1054000000
2254500000
"""
import sys
from collections import deque

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = K = -1
WIDE = 10


def bfs(sr, sc):
    grp = []

    que = deque()
    vis[sr][sc] = True
    que.append((sr, sc))
    grp.append((sr, sc))
    while que:
        cy, cx = que.popleft()
        for dy, dx in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ny, nx = cy + dy, cx + dx
            if not (0 <= ny < N and 0 <= nx < WIDE): continue
            if bd[ny][nx] == '0': continue
            if vis[ny][nx]: continue
            if bd[ny][nx] != bd[sr][sc]: continue

            vis[ny][nx] = True
            que.append((ny, nx))
            grp.append((ny, nx))

    if len(grp) >= K:
        for r, c in grp:
            bd[r][c] = '0'
        return True
    return False


def rmv_zero(col):
    rmved = ''.join(''.join(col).split('0'))
    zero_add = ['0' for _ in range(N - len(rmved))]
    return list(''.join(zero_add) + rmved)


def fall_through():
    c = 0
    for col in zip(*bd):
        new_col = rmv_zero(col)
        for i in range(len(new_col)):
            bd[i][c] = new_col[i]
        c += 1


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    bd = [list(input().rstrip()) for _ in range(N)]

    while True:
        vis = [[False for _ in range(WIDE)] for _ in range(N)]
        flag = False
        for r in range(N):
            for c in range(WIDE):
                if bd[r][c] == '0': continue

                if bfs(r, c):  # elimi
                    flag = True
        fall_through()

        if not flag:
            break

    for r in range(N):
        print(''.join(bd[r]))
