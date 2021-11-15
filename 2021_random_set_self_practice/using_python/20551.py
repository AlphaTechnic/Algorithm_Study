"""
input :
5 5
9
0
-1
3
2
-1
10
5
9
0

output :
0
-1
-1
4
1
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def binary_search(arr, val):
    l = 0
    r = len(arr) - 1
    mid_save = mid = (l + r) // 2
    while l <= r:
        if val <= arr[mid]:
            r = mid - 1
            mid_save = mid
            mid = (l + r) // 2
        elif val > arr[mid]:
            l = mid + 1
            mid = (l + r) // 2

    return mid_save


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    arr = [int(input()) for _ in range(N)]
    arr.sort()

    # print(arr)
    for _ in range(M):
        val = int(input())
        idx = binary_search(arr, val)
        if val == arr[idx]:
            print(idx)
        else:
            print(-1)
