"""
input :
ACAYKP
CAPCAK

output :
4
ACAK
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def gen_dp():
    for i in range(1, P + 1):
        for j in range(1, Q + 1):
            if A[i] != B[j]:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = dp[i - 1][j - 1] + 1


def dp_inverse():
    ans = ""
    cur = dp[-1][-1]
    y = len(dp) - 1
    x = len(dp[0]) - 1

    while cur != 0:
        if dp[y - 1][x] == cur - 1 and dp[y][x - 1] == cur - 1:
            ans = B[x] + ans
            cur -= 1; y -= 1; x -= 1  # 좌대각 이동
        elif dp[y - 1][x] > dp[y][x - 1]:
            y -= 1
        else:  # dp[y - 1][x] <= dp[x - 1][y]
            x -= 1

    return ans


if __name__ == "__main__":
    A = list(input().rstrip())
    B = list(input().rstrip())
    P, Q = len(A), len(B)
    A = ['_'] + A
    B = ['_'] + B

    # dp[i][j] = A[:i]와 B[:j]의 LCS의 길이
    dp = [[0 for _ in range(Q + 1)] for _ in range(P + 1)]

    gen_dp()
    print(dp[-1][-1])
    print(dp_inverse())
