"""
input :
26 11

output :
15 19
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def xGCD(a, b):
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    while b != 0:
        q = a // b
        a, b = b, a % b
        x1, x0 = x0 - q * x1, x1
        y1, y0 = y0 - q * y1, y1

    return a, x0, y0


if __name__ == "__main__":
    MOD, A = map(int, input().rstrip().split())

    Ap_inv = (MOD - A + MOD) % MOD

    Am_inv = -1
    g, x, y = xGCD(A, MOD)
    if g != 1:
        print(Ap_inv, -1)
    else:
        print(Ap_inv, (x + MOD) % MOD)
