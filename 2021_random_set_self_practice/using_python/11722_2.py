"""
input :
6
10 30 10 20 20 10

output :
3
"""
import sys
from bisect import bisect_left
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp = [(- nums[0], nums[0])]
    for num in nums:
        if num < dp[-1][1]:
            dp.append((- num, num))
        else:
            idx = bisect_left(dp, (- num, num))
            dp[idx] = (- num, num)
    print(len(dp))
