"""
input :
6
10 20 10 30 20 50

output :
4
10 20 30 50
"""
import sys
from collections import deque

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = [0] + list(map(int, input().rstrip().split()))

    par = [0 for _ in range(N + 1)]
    dp = [0 for _ in range(N + 1)]
    for i in range(N + 1):
        for j in range(i):
            if nums[j] < nums[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                par[i] = j

    res = deque()
    mxv = max(dp)
    idx = dp.index(mxv)
    while True:
        if par[idx] == 0:
            res.appendleft(nums[idx])
            break
        else:
            res.appendleft(nums[idx])
            idx = par[idx]
    print(len(res))
    print(' '.join(map(str, res)))
