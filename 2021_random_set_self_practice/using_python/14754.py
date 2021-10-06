"""
input :
4 4
1 2 4 6
16 9 13 11
5 10 8 15
12 14 7 3

output :
72
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline


def get_mxv(arr):
    return max(arr)


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    bd = [list(map(int, input().rstrip().split())) for _ in range(R)]

    tot = 0
    for r in range(R):
        for c in range(C):
            tot += bd[r][c]

    mxvs = set()
    # 가로 최대
    for r in range(R):
        mxvs.add(get_mxv(bd[r]))

    # 세로 최대
    for c in range(C):
        ln = []
        for r in range(R):
            ln.append(bd[r][c])
        mxvs.add(get_mxv(ln))

    print(tot - sum(mxvs))
