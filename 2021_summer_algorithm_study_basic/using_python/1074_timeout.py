"""
input:
2 3 1

output :
11
"""

import sys
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(r, c, SZ):
    global cnt; global qr; global qc;
    if SZ == 1:
        cnt += 1
        if [r, c] == [qr, qc]:
            print(cnt - 1)
        return

    recur(r, c, SZ // 2)
    recur(r, c + SZ // 2, SZ // 2)
    recur(r + SZ // 2, c, SZ // 2)
    recur(r + SZ // 2, c + SZ // 2, SZ // 2)


if __name__ == "__main__":
    N, qr, qc = map(int, input().rstrip().split())

    cnt = 0
    recur(0, 0, 2 ** N)