"""
input :
8

output :
92
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def mark(bd, r, c):
    global N
    bd[r][c] += 1
    for rr in range(r + 1, N):
        for cc in range(N):
            if rr + cc == r + c or rr - cc == r - c or cc == c:
                bd[rr][cc] += 1
    return bd


def unmark(bd, r, c):
    global N
    bd[r][c] -= 1
    for rr in range(r + 1, N):
        for cc in range(N):
            if rr + cc == r + c or rr - cc == r - c or cc == c:
                bd[rr][cc] -= 1
    return bd


def recur(bd, n):
    global N, g_cnt
    if n == N:
        return 1

    cnt = 0
    for i in range(N):
        if bd[n][i]: continue

        bd = mark(bd, n, i)
        cnt += recur(bd, n + 1)
        bd = unmark(bd, n, i)

    return cnt


if __name__ == "__main__":
    N = int(input())
    bd = [[0 for _ in range(N)] for _ in range(N)]
    print(recur(bd, 0))
