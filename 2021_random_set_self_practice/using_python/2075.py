"""
input :
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49

output :
35
"""
import sys
from heapq import *

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = []
    heapify(nums)

    for _ in range(N):
        tmp = list(map(int, input().rstrip().split()))
        for t in tmp:
            if len(nums) < N:
                heappush(nums, t)
            elif t > nums[0]:
                heappop(nums)
                heappush(nums, t)
    print(nums[0])
