"""
input :
7
15 11 18 16 14 10 19
4 1 3 9 5 11 2

output :
16 3
good
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def binary_search1(key, grps):
    if key < grps[0]:
        return -1

    l = 0
    r = len(grps) - 1
    mid_save = mid = (l + r) // 2
    while l <= r:
        if key >= grps[mid]:
            l = mid + 1
            mid_save = mid
            mid = (l + r) // 2
        else:
            r = mid - 1
            mid = (l + r) // 2
    return mid_save


def binary_search2(key, grps):
    if key > grps[-1]:
        return len(grps)

    l = 0
    r = len(grps) - 1
    mid_save = mid = (l + r) // 2
    while l <= r:
        if key <= grps[mid]:
            r = mid - 1
            mid_save = mid
            mid = (l + r) // 2
        else:
            l = mid + 1
            # mid_save = mid
            mid = (l + r) // 2
    return mid_save


if __name__ == "__main__":
    N = int(input())
    A_grps = list(map(int, input().rstrip().split()))
    B_grps = list(map(int, input().rstrip().split()))
    A_grps.sort()
    B_grps.sort()

    X = 1
    mxva = -1
    syma = -1
    while X <= A_grps[-1]:
        l = max(0, binary_search2(X - 2, A_grps))
        r = min(len(A_grps), binary_search1(X + 2, A_grps))

        if mxva < r - l + 1:
            mxva = r - l + 1
            syma = X
        # print(f"X = {X}, r - l = {r - l},  l={l}, r={r}")
        X += 1

    X = 1
    mxvb = -1
    symb = -1
    while X <= B_grps[-1]:
        l = max(0, binary_search2(X - 2, B_grps))
        r = min(len(A_grps), binary_search1(X + 2, B_grps))

        if mxvb < r - l + 1:
            mxvb = r - l + 1
            symb = X
        X += 1

    print(syma, symb)
    if syma > symb:
        print("good")
    else:
        print("bad")
