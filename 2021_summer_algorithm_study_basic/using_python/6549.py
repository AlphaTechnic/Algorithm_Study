"""
input :
7
2
1
4
5
1
3
3

output :
8
"""
import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
PIV = 1 << 17
MAX = 10 ** 9 + 5
TREE = [0 for _ in range(2 * PIV)]


def update(ind):
    ind += PIV
    TREE[ind] = ind - PIV

    while True:
        ind >>= 1
        if ind == 0: return
        if nums[TREE[2 * ind]] <= nums[TREE[2 * ind + 1]]:
            TREE[ind] = TREE[2 * ind]
        else:
            TREE[ind] = TREE[2 * ind + 1]


def query(l, r):
    l += PIV; r += PIV
    idx_of_min_val = 0
    while l <= r:
        if l & 1:
            if nums[idx_of_min_val] > nums[TREE[l]]:
                idx_of_min_val = TREE[l]
            l += 1
        if not r & 1:
            if nums[idx_of_min_val] > nums[TREE[r]]:
                idx_of_min_val = TREE[r]
            r -= 1
        l >>= 1; r >>= 1
    return idx_of_min_val


def divide_and_conquer(l, r):
    if l > r: return 0

    idx_of_min_val = query(l, r)
    case1 = (r - l + 1) * nums[idx_of_min_val]
    case2 = divide_and_conquer(l, idx_of_min_val - 1)
    case3 = divide_and_conquer(idx_of_min_val + 1, r)
    return max(case1, case2, case3)


if __name__ == "__main__":
    N = int(input())
    nums = [MAX] + [int(input()) for _ in range(N)]
    for i in range(1, N + 1):
        TREE[PIV + i] = i

    for i in range(1, N + 1):
        update(i)
    print(divide_and_conquer(1, N))
