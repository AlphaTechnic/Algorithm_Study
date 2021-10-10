"""
input:
10 6
1 3 10000
1 4 -5000
1 7 -3000
2 1 10
1 6 35000
2 4 10

output :
2000
27000
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline
PIV = 1 << 20
TREE = [0 for _ in range(2 * PIV)]


def update(idx, x):
    idx += PIV
    TREE[idx] += x
    while True:
        idx >>= 1
        if idx == 0:
            break
        TREE[idx] += x


def query(l, r):
    l += PIV
    r += PIV
    tot = 0
    while l <= r:
        if (l & 1) == 1:
            tot += TREE[l]
            l += 1
        if (r & 1) == 0:
            tot += TREE[r]
            r -= 1
        l >>= 1
        r >>= 1
    return tot


if __name__ == "__main__":
    N, Q = map(int, input().rstrip().split())

    for _ in range(Q):
        t, a, b = map(int, input().rstrip().split())
        if t == 1:
            update(a, b)

        elif t == 2:
            print(query(a, b))
