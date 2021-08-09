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
    global ans; global qr; global qc;
    if SZ == 1:
        return 0

    if r <= qr < r + SZ // 2 and c <= qc < c + SZ // 2:
        ans += recur(r, c, SZ // 2)
    elif r <= qr < r + SZ // 2 and c + SZ // 2 <= qc < c + SZ:
        ans += (SZ // 2) ** 2 + recur(r, c + SZ // 2, SZ // 2)
    elif r + SZ // 2 <= qr < r + SZ and c <= qc < c + SZ // 2:
        ans += 2 * ((SZ // 2) ** 2) + recur(r + SZ // 2, c, SZ // 2)
    else:
        ans += 3 * ((SZ // 2) ** 2) + recur(r + SZ // 2, c + SZ // 2, SZ // 2)

    return ans


if __name__ == "__main__":
    N, qr, qc = map(int, input().rstrip().split())

    ans = 0
    print(recur(0, 0, 2 ** N))