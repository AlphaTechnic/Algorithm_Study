"""
input :
5
8 9 1 2 10

output:
3
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    dp = [1 for _ in range(N)]

    for i in range(1, N):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
