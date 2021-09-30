"""
input :
3
26 40 83
49 60 57
13 89 99

output :
110
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
INF = 10 ** 9


def get_mnv(dp, a, b):
    dp[1][a] = dp[1][b] = INF

    for i in range(2, N + 1):
        for clr in range(3):
            if clr == 0:
                dp[i][clr] = dp[i][clr] + min(dp[i - 1][1], dp[i - 1][2])
            elif clr == 1:
                dp[i][clr] = dp[i][clr] + min(dp[i - 1][0], dp[i - 1][2])
            elif clr == 2:
                dp[i][clr] = dp[i][clr] + min(dp[i - 1][0], dp[i - 1][1])

    return min(dp[N][a], dp[N][b])


def cpy(dp):
    global N
    ret = [[0 for _ in range(3)] for _ in range(N + 1)]
    for r in range(len(dp)):
        for c in range(len(dp[0])):
            ret[r][c] = dp[r][c]
    return ret


if __name__ == "__main__":
    N = int(input())

    dp = [[0, 0, 0]] + [list(map(int, input().rstrip().split())) for _ in range(N)]
    dp_save = cpy(dp)

    case1 = get_mnv(dp, 1, 2)
    dp = cpy(dp_save)
    case2 = get_mnv(dp, 0, 2)
    dp = cpy(dp_save)
    case3 = get_mnv(dp, 0, 1)

    print(min(case1, case2, case3))
