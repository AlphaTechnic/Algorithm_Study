import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def mk_dp(N):
    dp = [[1 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(2, N + 1):
        for j in range(1, i):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp


if __name__ == "__main__":
    CNTA, CNTZ, k = map(int, input().rstrip().split())

    # make dp
    N = CNTA + CNTZ
    dp = mk_dp(N)
    if k > dp[N][CNTA]:
        print(-1)
        exit(0)

    ans = ""
    accumulated = 0
    cnt_a = 0
    cnt_z = 0
    while cnt_a != CNTA or cnt_z != CNTZ:
        remain_a = CNTA - cnt_a
        remain_z = CNTZ - cnt_z

        # a를 놓았다는 가정을 해봤을 때,
        if accumulated + dp[(remain_a - 1) + remain_z][(remain_a - 1)] >= k and cnt_a < CNTA:  # a가 놓여 있는게 맞는 상황
            ans += 'a'
            cnt_a += 1
        else:  # a가 아닌 z를 놓는게 마따~
            ans += 'z'
            cnt_z += 1

            # a를 놓은 경우의 수는 accumulated에 누적 시킴
            accumulated += dp[(remain_a - 1) + remain_z][remain_a - 1]

    print(ans)
