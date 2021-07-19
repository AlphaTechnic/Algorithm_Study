"""
input :
10 3
3
4
5
6
7
8
9
10
11
12

output :
60
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

PIV = 1 << 18
tree = [0 for _ in range(2 * PIV)]


def query(mid_ind):
    idx = 1
    while idx < PIV:
        idx <<= 1
        if tree[idx] < mid_ind:
            mid_ind -= tree[idx]
            idx += 1
    return idx - PIV


def update(num, chk):
    num += PIV
    tree[num] += chk
    while True:
        num >>= 1
        if num == 0: break

        tree[num] += chk


if __name__ == "__main__":
    N, K = map(int, input().rstrip().split())

    back_up = []
    for i in range(K):
        num = int(input())
        back_up.append(num)
        update(num, 1)

    ans = 0
    try:
        for i in range(K, N + 1):
            mid = query((K + 1) // 2)
            ans += mid

            update(back_up[i - K], -1)
            num = int(input())
            back_up.append(num)
            update(num, 1)
    except:
        pass

    print(ans)