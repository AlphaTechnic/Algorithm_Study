"""
input :
7
3 1 1 7 4 9 3

output :
5
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    if N <= 2:
        print(0)
        exit(0)

    dp = list(map(int, input().rstrip().split()))
    for i in range(3, N):
        dp[i] += min(dp[i - 1], dp[i - 2], dp[i - 3])
    print(min(dp[-1], dp[-2], dp[-3]))
