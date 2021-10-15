"""
input :
6
10 20 10 30 20 50

output :
4
"""
import sys
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp = [1 for _ in range(N)]
    for i in range(1, N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    L = max(dp)
    print(L)

    ans = deque()
    for i in range(len(dp) - 1, -1, -1):
        if dp[i] == L:
            ans.appendleft(nums[i])
            L -= 1
    print(' '.join(map(str, ans)))
