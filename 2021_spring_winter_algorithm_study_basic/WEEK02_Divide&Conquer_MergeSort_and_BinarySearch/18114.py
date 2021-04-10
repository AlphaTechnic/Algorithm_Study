"""
input :
5 5
1 2 3 4 5
"""

import sys
import bisect
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


N, M = map(int, input().rstrip().split())
nums = set()
for num in map(int, input().split()):
    nums.add(num)

# 1개 조합
if M in nums:
    print(1)
    exit()

# 2개 조합
for num in nums:
    if M > num:
        target = M - num
        if target in nums and num != target:
            print(1)
            exit()


# 3개 조합
num_list = list(nums)
for i in range(N):
    for j in range(i+1, N):
        if M > num_list[i] + num_list[j]:
            target = M - (num_list[i] + num_list[j])
            if target in nums and num_list[i] != target and num_list[j] != target:
                print(1)
                exit()

print(0)
