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


def add2(txt):
    return int(txt) + 2


def idx_of_mxv(grp):
    chk = [0 for _ in range(10 ** 5 + 10)]
    for num in grp:
        chk[num - 2] += 1
        chk[num + 3] -= 1

    cum_sum = []
    tot = 0
    for val in chk:
        tot += val
        cum_sum.append(tot)

    mxa = -1
    ans_idx = -1
    for i in range(grp[0] - 2, grp[-1] + 3):
        if cum_sum[i] > mxa:
            mxa = cum_sum[i]
            ans_idx = i - 2
    return ans_idx


if __name__ == "__main__":
    N = int(input())
    grpA = list(map(add2, input().rstrip().split()))
    grpB = list(map(add2, input().rstrip().split()))
    grpA.sort()
    grpB.sort()

    a = idx_of_mxv(grpA)
    b = idx_of_mxv(grpB)
    print(a, b)
    print("good") if a > b else print("bad")
