import sys

sys.setrecursionlimit(10 ** 4)
sys.stdin.readline = input
sys.stdin = open("input.txt", "r")


def func(l, r, turn):
    if l == r:
        if turn == 0:
            return cards[l]
        else:
            return 0

    if dp[l][r] != -1:
        return dp[l][r]

    if turn == 0:
        dp[l][r] = max(func(l + 1, r, (turn + 1) % 2) + cards[l], func(l, r - 1, (turn + 1) % 2) + cards[r])
    else:
        dp[l][r] = min(func(l + 1, r, (turn + 1) % 2), func(l, r - 1, (turn + 1) % 2))

    return dp[l][r]


T = int(input())
for _ in range(T):
    N = int(input())
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    cards = [int(n) for n in input().split()]
    print(func(0, N - 1, 0))
