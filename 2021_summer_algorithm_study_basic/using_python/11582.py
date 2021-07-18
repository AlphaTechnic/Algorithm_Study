"""
input :
8
1 5 2 4 2 9 7 3
2

output :
1 2 4 5 2 3 7 9
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def merge(s, e):
    if e - s > N // K: return  # 좌변 == 구간길이

    mid = (s + e) // 2
    idx1 = idx3 = s; idx2 = mid + 1;

    while idx1 <= mid and idx2 <= e:
        if nums[idx1] < nums[idx2]:
            tmp[idx3] = nums[idx1]
            idx3 += 1; idx1 += 1;
        else:  # nums[idx1] >= nums[idx2]
            tmp[idx3] = nums[idx2]
            idx3 += 1; idx2 += 1;

    while idx1 <= mid:
        tmp[idx3] = nums[idx1]
        idx3 += 1; idx1 += 1;

    while idx2 <= e:
        tmp[idx3] = nums[idx2]
        idx3 += 1; idx2 += 1;

    for i in range(s, e + 1):
        nums[i] = tmp[i]


def merge_sort(s, e):
    if s == e: return

    mid = (s + e) // 2
    merge_sort(s, mid)
    merge_sort(mid + 1, e)
    merge(s, e)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))
    K = int(input())

    tmp = [0 for _ in range(N)]
    merge_sort(0, N - 1)

    for num in nums:
        print(num, end=' ')
