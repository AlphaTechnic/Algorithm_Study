"""
input :
9 3
1 2 3 4 5 6 7 8 9

output :
17
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    nums = list(map(int, input().rstrip().split()))

    l = max(nums)
    r = 10 ** 8 + 5
    mid_save = mid = (l + r) // 2

    while l <= r:
        blueray_list = []
        tot = 0
        for i, num in enumerate(nums):
            tot += num
            if tot > mid:
                tot -= num
                blueray_list.append(tot)
                tot = num
            if i == len(nums) - 1:
                blueray_list.append(tot)
        if len(blueray_list) <= M:
            mid_save = mid
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2

    print(mid_save)