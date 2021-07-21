"""
input :
3
5 3
3 2
2 6

output :
90
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


class Interval():
    def __init__(self, l, r):
        self.l = l
        self.r = r


def recur(a, b):
    ret = 1 << 31
    if b - a == 1:
        return arr[a].l * arr[a].r * arr[b].r
    if a == b:
        return 0

    if dp[a][b] != 0:
        return dp[a][b]

    for i in range(a, b):
        lc = recur(a, i)
        rc = recur(i + 1, b)
        mid = arr[i].r
        ret = min(ret, lc + rc + arr[a].l * mid * arr[b].r)

    dp[a][b] = ret
    return dp[a][b]


if __name__ == "__main__":
    N = int(input())

    arr = ['_']
    for _ in range(1, N + 1):
        a, b = map(int, input().rstrip().split())
        interval_obj = Interval(a, b)
        arr.append(interval_obj)

    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    ans = recur(1, N)

    print(ans)
