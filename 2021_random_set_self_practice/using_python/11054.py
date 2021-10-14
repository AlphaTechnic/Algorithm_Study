"""
input :
10
1 5 2 1 4 3 4 5 2 1

output :
7
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

PIV = 1 << 10
MAX = 1000
TREE = [0 for _ in range(2 * PIV)]


def update(idx, x):
    idx += PIV
    TREE[idx] = x
    while True:
        idx >>= 1
        if idx == 0:
            break
        TREE[idx] = max(TREE[2 * idx], TREE[2 * idx + 1])


def query(l, r):
    l += PIV
    r += PIV
    ret = 0
    while l <= r:
        if (l & 1) == 1:
            ret = max(ret, TREE[l])
            l += 1
        if (r & 1) == 0:
            ret = max(ret, TREE[r])
            r -= 1
        l >>= 1
        r >>= 1
    return ret


def get_mxv_of_sum(arr1, arr2):
    mxv = -1
    for i in range(len(arr1)):
        mxv = max(mxv, arr1[i] + arr2[i])
    return mxv


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    dp1 = [1 for _ in range(N)]
    for i, num in enumerate(nums):
        q = query(0, num - 1)
        update(num, q + 1)
        dp1[i] = q + 1

    TREE = [0 for _ in range(2 * PIV)]

    dp2 = [1 for _ in range(N)]
    for i in range(N - 1, -1, -1):
        q = query(0, nums[i] - 1)
        update(nums[i], q + 1)
        dp2[i] = q + 1

    print(get_mxv_of_sum(dp1, dp2) - 1)
