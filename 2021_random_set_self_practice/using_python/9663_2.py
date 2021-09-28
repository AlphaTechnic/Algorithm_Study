"""
input :
8

output :
92
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
col_used = [False for _ in range(N)]
rd_used = [False for _ in range(2 * N + 1)]
ld_used = [False for _ in range(2 * N + 1)]


def mark(r, c):
    global N
    col_used[c] = True
    rd_used[r + c] = True
    ld_used[r - c + (N - 1)] = True


def unmark(r, c):
    global N
    col_used[c] = False
    rd_used[r + c] = False
    ld_used[r - c + (N - 1)] = False


def is_used(r, c):
    return col_used[c] or rd_used[r + c] or ld_used[r - c + (N - 1)]


def recur(r):
    global N
    if r == N:
        return 1

    cnt = 0
    for i in range(N):
        if is_used(r, i): continue

        mark(r, i)
        cnt += recur(r + 1)
        unmark(r, i)

    return cnt


if __name__ == "__main__":
    print(recur(0))