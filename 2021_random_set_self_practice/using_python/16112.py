"""
input :
3 2
100 300 200

output :
800
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    p = 1
    tot = 0
    for i in range(1, len(nums)):
        tot += nums[i] * p
        p = min(p + 1, K)

    print(tot)
