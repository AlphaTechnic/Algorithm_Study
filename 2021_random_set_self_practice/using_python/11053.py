"""
input :
6
10 20 10 30 20 50

output :
4
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp = [1 for _ in range(N)]
    for i in range(N):
        for j in range(i - 1, -1, -1):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
