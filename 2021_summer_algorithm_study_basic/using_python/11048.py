"""
input :
3 4
1 2 3 4
0 0 0 5
9 8 7 6

output :
31
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    dp = [[0 for _ in range(M + 1)]]
    for _ in range(N):
        dp.append([0] + list(map(int, input().rstrip().split())))

    for r in range(1, N + 1):
        for c in range(1, M + 1):
            dp[r][c] = max(dp[r - 1][c - 1], dp[r - 1][c], dp[r][c - 1]) + dp[r][c]

    print(dp[N][M])
