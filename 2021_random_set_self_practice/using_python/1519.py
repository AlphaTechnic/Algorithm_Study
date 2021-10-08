"""
input :
17

output:
-1
"""
import sys

sys.stdin = open("input.txt", 'r')
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

INF = 10 ** 8


def recur(N):
    if N < 10:
        dp[N] = 0
        return 0
    if dp[N] != -1:
        return dp[N]

    N_str = str(N)
    flag = 0
    for i in range(1, len(N_str) + 1):
        for j in range(i):
            sbstr_num = N % 10 ** i // 10 ** j
            if not 0 < sbstr_num < N: continue

            nxt = N - sbstr_num
            if recur(nxt) == 0:
                flag = 1
                break
        if flag:
            break

    dp[N] = flag
    return dp[N]


if __name__ == "__main__":
    N = int(input())
    dp = [-1 for _ in range(N + 1)]

    recur(N)

    if dp[N] == 0:
        print(-1)

    else:
        N_str = str(N)
        for i in range(10):
            dp[i] = 0

        ans = INF
        for i in range(1, len(N_str) + 1):
            for j in range(i):
                sbstr_num = N % 10 ** i // 10 ** j
                if not 0 < sbstr_num < N: continue

                nxt = N - sbstr_num
                if recur(nxt) == 0:
                    ans = min(ans, sbstr_num)

        print(ans)
