"""
input :
6
5 10 -2 3 5 2

output :
250
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    mxv1 = max(nums[0] * nums[1], nums[0] * nums[1] * nums[2], nums[-1] * nums[-2], nums[-1] * nums[-2] * nums[-3])
    mxv2 = max(nums[0] * nums[1] * nums[-1], nums[0] * nums[-1] * nums[-2])
    print(max(mxv1, mxv2))
