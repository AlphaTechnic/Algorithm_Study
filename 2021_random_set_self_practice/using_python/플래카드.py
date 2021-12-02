"""
input :
9
7 3 8 4 5 2 6 8 1

output :
49
1 8
"""
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    l = 0
    r = len(nums) - 1
    mxv = -1
    ans_l = -1
    ans_r = -1
    while l <= r:
        area = (r - l) * min(nums[l], nums[r])
        if area > mxv:
            mxv = area
            ans_l = l
            ans_r = r

        if nums[l] <= nums[r]:
            l += 1
        elif nums[l] > nums[r]:
            r -= 1

    print(mxv)
    print(ans_l + 1, ans_r + 1)
