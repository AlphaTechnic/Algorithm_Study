"""
input :
6
10 -5 3 2 4 -7

output :
14
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def divide_and_conquer(nums, l, r):
    if l == r:
        return nums[l]

    mid = (l + r) // 2

    # case 1
    max_left_sum = - 10 ** 10
    tmp_left_sum = 0
    for i in range(mid, l - 1, -1):
        tmp_left_sum += nums[i]
        max_left_sum = max(max_left_sum, tmp_left_sum)
    max_right_sum = - 10 ** 10
    tmp_right_sum = 0
    for i in range(mid + 1, r + 1):
        tmp_right_sum += nums[i]
        max_right_sum = max(max_right_sum, tmp_right_sum)
    case1 = max_left_sum + max_right_sum

    # case 2, case 3
    case2 = divide_and_conquer(nums, l, mid)
    case3 = divide_and_conquer(nums, mid + 1, r)

    return max(case1, case2, case3)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    print(divide_and_conquer(nums, 0, len(nums) - 1))
