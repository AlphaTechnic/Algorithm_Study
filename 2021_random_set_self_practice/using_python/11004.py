"""
input :
5 2
4 1 2 3 5

output :
2
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    print(nums[K - 1])
