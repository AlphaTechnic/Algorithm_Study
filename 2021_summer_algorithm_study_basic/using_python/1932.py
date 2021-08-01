"""
input :
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5

output :
30
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        nums = [0] + list(map(int, input().rstrip().split()))
        for j in range(1, i + 1):
            dp[i][j] = nums[j]

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + dp[i][j]

    print(max(dp[N]))