"""
input :
7
4 2 7 1 5 6 3

output :
10
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
PIV = 1 << 21
tree = [0 for _ in range(PIV << 1)]


def update(idx, update_value):
    idx += PIV
    tree[idx] += update_value
    while True:
        idx >>= 1
        if idx == 0:
            break
        tree[idx] += update_value


def query(idx):
    l = PIV
    r = idx + PIV

    ret = 0
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if (r & 1) == 0:
            ret += tree[r]
            r -= 1
        l >>= 1
        r >>= 1

    return ret


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    ans = 0
    for i in range(len(nums) - 1, -1, -1):
        update(nums[i], 1)
        ans += query(nums[i] - 1)

    print(ans)