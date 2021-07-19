"""
input :
5 6
1 5
2 2
3 2
4 3
5 1
5 3

output :
8
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

PIV = 1 << 11
tree = [0 for _ in range(PIV << 1)]


def update(a):
    a += PIV
    tree[a] += 1
    while True:
        a >>= 1
        if a == 0: break

        tree[a] += 1


def query(a, b):
    ret = 0

    a += PIV; b += PIV
    while a <= b:
        if a & 1 == 1: ret += tree[a]; a += 1
        if b & 1 == 0: ret += tree[b]; b -= 1
        a >>= 1; b >>= 1

    return ret


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())

    match = []
    for _ in range(M):
        match.append(list(map(int, input().rstrip().split())))

    match.sort()

    ans = 0
    for a, b in match:
        update(b)
        ans += query(b + 1, N)

    print(ans)
