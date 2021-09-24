"""
input :
6
6
4
5
5
5
5

output :
21
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list()
    for _ in range(N):
        nums.append((int(input())))

    nums.sort(reverse=True)
    tot = sum(nums)
    for i in range(2, N, 3):
        tot -= nums[i]
    print(tot)
