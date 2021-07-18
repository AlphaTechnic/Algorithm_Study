"""
input :
7
3 1 6 2 7 30 1

output :
21
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().rstrip().split()))
nums.sort()

tot = 0
for num in nums:
    limit = tot + 1
    if num <= limit:
        tot += num
    else:
        break
print(tot + 1)