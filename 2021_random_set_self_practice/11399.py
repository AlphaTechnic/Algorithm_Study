"""
input :
5
3 1 4 3 2

output :
32
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    nums.sort()

    cumulative_sum = list()
    tot = 0
    for num in nums:
        tot += num
        cumulative_sum.append(tot)
    print(sum(cumulative_sum))
