import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_list = list(map(int, input().split()))
M = int(input())
target_list = list(map(int, input().split()))

num_list.sort()
for target in target_list:
    left = 0
    right = N - 1

    while left <= right:
        mid = (left + right) // 2
        if mid >= N:
            break
        if target < num_list[mid]:
            right = mid - 1
        elif target > num_list[mid]:
            left = mid + 1
        else: # target == num_list[mid]
            break

    if target == num_list[mid]:
        print(1)
    else:
        print(0)
