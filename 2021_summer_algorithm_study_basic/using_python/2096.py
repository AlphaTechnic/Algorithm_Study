"""
input :
3
0 0 0 0 0
0 1 2 3 0
0 4 5 6 0
0 4 9 0 0

output :
18 6
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def cal1(max_dp):
    for c in range(1, 4):
        max_dp[1][c] = max(max_dp[0][c - 1], max_dp[0][c], max_dp[0][c + 1]) + max_dp[1][c]


def cal2(min_dp):
    for c in range(1, 4):
        min_dp[1][c] = min(min_dp[0][c - 1], min_dp[0][c], min_dp[0][c + 1]) + min_dp[1][c]


def mov_up(dp):
    dp[0] = dp[1]
    del dp[1]


if __name__ == "__main__":
    N = int(input())
    max_dp = [[0 for _ in range(5)]]
    min_dp = [[0 for _ in range(5)]]
    for _ in range(N):
        tmp = list(map(int, input().rstrip().split()))
        max_dp.append([0] + tmp + [0])
        min_dp.append([10 ** 9] + tmp + [10 ** 9])

        cal1(max_dp); cal2(min_dp);
        mov_up(max_dp); mov_up(min_dp);

    print(max(max_dp[-1]), min(min_dp[-1]))
