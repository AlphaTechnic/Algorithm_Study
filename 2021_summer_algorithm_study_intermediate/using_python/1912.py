"""
input :
10
10 -4 3 1 5 6 -35 12 21 -1

output :
33
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def get_center_max(l, mid, r):
    left_max = ~(1 << 27)
    left_sum = 0
    for i in range(mid, l - 1, -1):
        left_sum += nums[i]
        left_max = max(left_max, left_sum)

    right_max = ~(1 << 27)
    right_sum = 0
    for i in range(mid + 1, r + 1):
        right_sum += nums[i]
        right_max = max(right_max, right_sum)

    return left_max + right_max


def recur(l, r):
    if l == r:
        return nums[l]

    mid = (l + r) // 2
    left_max = recur(l, mid)
    right_max = recur(mid + 1, r)
    center_max = get_center_max(l, mid, r)

    return max(left_max, right_max, center_max)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    max_val = recur(0, N - 1)
    print(max_val)