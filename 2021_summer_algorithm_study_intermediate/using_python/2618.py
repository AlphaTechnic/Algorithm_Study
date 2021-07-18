"""
input :
6
3
3 5
5 5
2 3

output :
9
2
2
1
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def gen_dp(c1, c2):
    cur = max(c1, c2)  # 현재까지 처리한 사건
    if cur == W + 2:  # 사건을 모두 처리한 후에 W + 2 번째 사건을 처리하려고 하면 종료
        return 0

    if dp[c1][c2] != -1:  # memo
        return dp[c1][c2]

    # 경찰차 1이 다음 사건 처리
    case1 = gen_dp(cur + 1, c2) + dist(pos[cur + 1], pos[c1])
    # 경찰차 2가 다음 사건 처리
    case2 = gen_dp(c1, cur + 1) + dist(pos[cur + 1], pos[c2])
    dp[c1][c2] = min(case1, case2)
    return dp[c1][c2]


def print_path(c1, c2):
    cur = max(c1, c2)
    if cur == W + 2: return

    case1 = dp[cur + 1][c2] + dist(pos[cur + 1], pos[c1])
    case2 = dp[c1][cur + 1] + dist(pos[cur + 1], pos[c2])
    if case1 < case2:
        print(1)
        print_path(cur + 1, c2)
    else:
        print(2)
        print_path(c1, cur + 1)


if __name__ == "__main__":
    N = int(input())
    W = int(input())
    pos = []

    pos.append(['_', '_'])  # 0번째 인덱스는 사용하지 않는다.
    pos.append([1, 1])
    pos.append([N, N])
    # W개의 사건 발생
    for _ in range(W):
        a, b = map(int, input().rstrip().split())
        pos.append([a, b])

    # dp[i][j] : 경찰차 1이 i번째, 경찰차 2가 j번째 사건 담당시 이동한 최소거리
    dp = [[-1 for _ in range(W + 3)] for _ in range(W + 3)]

    print(gen_dp(1, 2))
    print_path(1, 2)