"""
input :
2
4
1 2 5 2
9
1 1 1 1 2 2 2 2 2

output :
6
8
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(l, r):
    if l > r: return 0
    if dp[l][r] != 0: return dp[l][r]

    if r - l <= 1:  # 카드가 2장 남음
        dp[l][r] = max(cards[l], cards[r])
        return dp[l][r]

    # 근우 왼 -> 승우 그 다음 뽑
    case1 = cards[l] + min(recur(l + 2, r), recur(l + 1, r - 1))
    # 근우 오른 -> 승우 그 다음 뽑
    case2 = cards[r] + min(recur(l, r - 2), recur(l + 1, r - 1))
    dp[l][r] = max(case1, case2)

    return dp[l][r]


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        cards = list(map(int, input().rstrip().split()))

        dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
        print(recur(0, N - 1))
