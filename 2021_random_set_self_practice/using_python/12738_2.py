"""
input :
6
10 20 10 30 20 50

output :
4
"""
import sys
from bisect import bisect_left
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    seq = [nums[0]]
    for num in nums:
        if num > seq[-1]:
            seq.append(num)
        else:
            idx = bisect_left(seq, num)
            seq[idx] = num
    print(len(seq))
