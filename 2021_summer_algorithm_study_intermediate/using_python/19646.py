"""
input :
5
1 2 3 4 5
6 4 6 1 2

output :
3 4 5 1 2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

PIV = 1 << 18
tree = [0 for _ in range(2 * PIV)]


def update(ind, val):
    ind += PIV
    tree[ind] += val

    while True:
        ind >>= 1
        if ind == 0: return
        tree[ind] += val


def query(l, r):
    l += PIV; r += PIV;
    ret = 0
    while l <= r:
        if l & 1:
            ret += tree[l]
            l += 1
        if not r & 1:
            ret += tree[r]
            r -= 1
        l >>= 1; r >>= 1;
    return ret


def search(k):
    ind = 1
    while not PIV <= ind:
        if k <= tree[ind << 1]:
            ind <<= 1
        else:
            k = k - tree[ind << 1]
            ind = (ind << 1) + 1

    return ind - PIV


if __name__ == "__main__":
    N = int(input())
    lengths = list(map(int, input().rstrip().split()))
    kths = list(map(int, input().rstrip().split()))

    for i, length in enumerate(lengths):
        update(i + 1, length)

    for kth in kths:
        num = search(kth)
        print(num, end=' ')
        update(num, - tree[PIV + num])
