"""
input :
10 11 12

output :
4
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(a, b):
    global mod
    if b == 0: return 1

    x = recur(a, b // 2)
    x = ((x % mod) * (x % mod)) % mod

    if b & 1: x = (x * a) % mod
    return x


if __name__ == "__main__":
    a, b, mod = map(int, input().rstrip().split())
    ans = recur(a, b)
    print(ans)
