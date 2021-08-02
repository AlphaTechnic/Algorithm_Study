"""
input :
13 5
4 6 7 11 12

output :
62000
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def recur(day, coupon):
    if day >= N + 1: return 0
    if dp[day][coupon] != -1: return dp[day][coupon]

    if DAY_OFF[day] == 1:
        ret = recur(day + 1, coupon)
    else:
        a = recur(day + 1, coupon) + 10000
        b = recur(day + 3, coupon + 1) + 25000
        c = recur(day + 5, coupon + 2) + 37000
        ret = min(a, b, c)

        if coupon >= 3:
            ret = min(ret, recur(day + 1, coupon - 3))

    dp[day][coupon] = ret
    return dp[day][coupon]


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    tmp = list(map(int, input().rstrip().split()))
    DAY_OFF = [0 for _ in range(N + 1)]
    for day in tmp:
        DAY_OFF[day] += 1

    dp = [[-1 for _ in range(N + 1)] for _ in range(N + 1)]

    print(recur(1, 0))
