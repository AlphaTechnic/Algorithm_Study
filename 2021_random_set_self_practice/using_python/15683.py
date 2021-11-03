"""
input :
6 6
0 0 0 0 0 0
0 2 0 0 0 0
0 0 0 0 6 0
0 6 0 0 2 0
0 0 0 0 0 0
0 0 0 0 0 5

output :
15
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
INF = 10 ** 9

ANS = INF
DIR = {1: [[0], [1], [2], [3]],
       2: [[0, 2], [1, 3]],
       3: [[0, 1], [1, 2], [2, 3], [3, 0]],
       4: [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
       5: [[0, 1, 2, 3], ]}


def cnt_zero(bd):
    cnt = 0
    for r in range(R):
        for c in range(C):
            if bd[r][c] == 0:
                cnt += 1
    return cnt


def erase(bd, ccy, ccx, dir):
    global R, C
    if dir == 0:
        if ccx + 1 < C:
            for c in range(ccx + 1, C):
                if bd[ccy][c] == 6:
                    break
                elif 1 <= bd[ccy][c] <= 5:
                    pass
                else:
                    bd[ccy][c] = -1
    elif dir == 1:
        if ccy + 1 < R:
            for r in range(ccy + 1, R):
                if bd[r][ccx] == 6:
                    break
                elif 1 <= bd[r][ccx] <= 5:
                    pass
                else:
                    bd[r][ccx] = -1
    elif dir == 2:
        if ccx - 1 >= 0:
            for c in range(ccx - 1, -1, -1):
                if bd[ccy][c] == 6:
                    break
                elif 1 <= bd[ccy][c] <= 5:
                    pass
                else:
                    bd[ccy][c] = -1
    else:
        if ccy - 1 >= 0:
            for r in range(ccy - 1, -1, -1):
                if bd[r][ccx] == 6:
                    break
                elif 1 <= bd[r][ccx] <= 5:
                    pass
                else:
                    bd[r][ccx] = -1


def dfs(bd, cnt):
    global ANS
    if cnt == cctv_cnt:
        # for r in range(R):
        #     for c in range(C):
        #         print(bd[r][c], end=' ')
        #     print()
        # print()

        ANS = min(ANS, cnt_zero(bd))
        return

    r, c = pos[cnt]
    type = bd[r][c]
    for dirs in DIR[type]:
        bd_save = [[bd[r][c] for c in range(C)] for r in range(R)]
        for dir in dirs:
            erase(bd, r, c, dir)

        dfs(bd, cnt + 1)

        bd = [[bd_save[r][c] for c in range(C)] for r in range(R)]


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    bd = [list(map(int, input().rstrip().split())) for _ in range(R)]

    pos = []
    for r in range(R):
        for c in range(C):
            if bd[r][c] != 6 and bd[r][c] != 0:
                pos.append((r, c))
    cctv_cnt = len(pos)

    dfs(bd, 0)
    print(ANS)
