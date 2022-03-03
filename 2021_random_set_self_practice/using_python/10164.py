"""
input :
3 5 8

output :
9
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def num2coord(num, X):
    if num == 0:
        return 0, 0

    y = (num - 1) // X
    x = (num - 1) % X
    return y, x


def set_combi(Y, X):
    lim = Y + X + 1
    dp = [[1 for _ in range(lim)] for _ in range(lim)]
    for i in range(1, lim):
        for j in range(i + 1):
            if j != 0 and j != i:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp


if __name__ == "__main__":
    Y, X, num = map(int, input().rstrip().split())
    if num == 0:
        num = 1

    combi = set_combi(Y, X)
    y, x = num2coord(num, X)

    val1 = combi[x + y][x]
    val2 = combi[X + Y - x - y - 2][X - x - 1]
    print(val1 * val2)
