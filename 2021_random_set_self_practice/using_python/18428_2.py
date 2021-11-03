"""
input :
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

output :
YES
"""
import sys
from itertools import combinations

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

RES = False
dir = [[0, 1], [1, 0], [0, -1], [-1, 0]]


def chk(cy, cx):
    cy_save, cx_save = cy, cx
    for i in range(4):
        cy, cx = cy_save, cx_save
        dy, dx = dir[i]
        while True:
            cy, cx = cy + dy, cx + dx
            if not (0 <= cy < N and 0 <= cx < N): break
            if bd[cy][cx] == 'O': break
            if bd[cy][cx] == 'S': return False
    return True


def is_blocked():
    for i in range(len(T_poses)):
        r, c = T_poses[i]
        happy = chk(r, c)
        if not happy:
            return False
    return True


if __name__ == "__main__":
    N = int(input())
    bd = [input().rstrip().split() for _ in range(N)]

    S_poses = []
    T_poses = []
    for r in range(N):
        for c in range(N):
            if bd[r][c] == 'X':
                S_poses.append((r, c))
            elif bd[r][c] == 'T':
                T_poses.append((r, c))

    res = False
    for combi in combinations(S_poses, 3):
        for y, x in combi:
            bd[y][x] = 'O'

        if is_blocked():
            res = True
            break

        for y, x in combi:
            bd[y][x] = 'X'

    print("YES") if res else print("NO")
