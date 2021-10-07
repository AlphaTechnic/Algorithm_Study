"""
input :
2
4 3 2 1 0 4 3 2 1
1 2 3 4 1 2 3 4 0

ouput :
46
"""
import sys
from itertools import permutations

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

mound = [0, 0, 0, 0]


def hit(p):
    global mound

    mound[0] = 1
    if p == 1:
        score = mound[3]
        mound[0], mound[1], mound[2], mound[3] = 0, mound[0], mound[1], mound[2]
    elif p == 2:
        score = mound[2] + mound[3]
        mound[0], mound[1], mound[2], mound[3] = 0, 0, mound[0], mound[1]
    elif p == 3:
        score = mound[1] + mound[2] + mound[3]
        mound[0], mound[1], mound[2], mound[3] = 0, 0, 0, mound[0]
    else:
        score = mound[0] + mound[1] + mound[2] + mound[3]
        mound = [0, 0, 0, 0]
    return score


def do_one_inning(seq, idx):
    tot = 0
    out_cnt = 0
    while out_cnt < 3:
        if seq[idx] == 0:
            out_cnt += 1
        else:
            tot += hit(seq[idx])

        idx = (idx + 1) % 9
    return tot, idx


def mk_seq(order, itr):
    return [itr[order[i]] for i in range(len(order))]


if __name__ == "__main__":
    N = int(input())
    rounds = [list(map(int, input().rstrip().split())) for _ in range(N)]

    mxv = 0
    for order in permutations(range(1, 9)):
        order = list(order)
        order = order[:3] + [0] + order[3:]

        idx = 0
        tot = 0
        for itr in rounds:
            mound = [0, 0, 0, 0]
            seq = mk_seq(order, itr)
            score, idx = do_one_inning(seq, idx)
            tot += score
        mxv = max(mxv, tot)

    print(mxv)
