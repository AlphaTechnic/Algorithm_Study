import sys
sys.stdin = open("input.txt", "r")

N = int(input())
num_list = list(map(int, input().split()))
num_list.sort()

left = 0
right = N-1
cnt = 0
for ind, target_num in enumerate(num_list):
    while left < right:
        Sum = num_list[left] + num_list[right]
        if left == ind:
            left += 1
            continue
        if right == ind:
            right -= 1
            continue

        if Sum < target_num:
            left += 1
        elif Sum > target_num:
            right -= 1
        else: # Sum == target_num:
            cnt += 1
            break
    left = 0
    right = N-1

print(cnt)
