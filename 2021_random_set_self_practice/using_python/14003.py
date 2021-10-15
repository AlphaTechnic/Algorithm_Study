"""
input :
6
10 20 10 30 20 50

output :
4
10 20 30 50
"""
import sys
from bisect import bisect_left
from collections import deque
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    mxv = 1
    dp = [1 for _ in range(N)]
    seq = [nums[0]]
    for i, num in enumerate(nums):
        if num > seq[-1]:
            seq.append(num)
            dp[i] = len(seq)
        else:
            idx = bisect_left(seq, num)
            seq[idx] = num
            dp[i] = idx + 1
        mxv = max(mxv, dp[i])

    L = mxv
    print(L)
    ans = deque()
    for i in range(len(dp) - 1, -1, -1):
        if dp[i] == L:
            ans.appendleft(nums[i])
            L -= 1
    print(' '.join(map(str, ans)))
