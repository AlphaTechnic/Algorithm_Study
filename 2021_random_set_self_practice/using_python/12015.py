"""
input :
6
10 20 10 30 20 50

output :
4
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

PIV = 1 << 20
TREE = [0 for _ in range(2 * PIV)]


def update(idx, x):
    idx += PIV
    TREE[idx] = x
    while True:
        idx >>= 1
        if idx == 0:
            return
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


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    mxv = 0
    for num in nums:
        q = query(0, num - 1)
        update(num, q + 1)
        mxv = max(mxv, q + 1)
    print(mxv)
