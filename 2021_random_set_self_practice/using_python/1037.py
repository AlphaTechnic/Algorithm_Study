"""
input :
4
2 3 4 6

output :
12
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    print(nums[0] * nums[-1])
