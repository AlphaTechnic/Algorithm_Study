"""
input :
4 4
0100
0111
1110
0010

output :
4
"""
import sys

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    bd = [list(map(int, list(input().rstrip()))) for _ in range(R)]

    for r in range(1, R):
        for c in range(1, C):
            if bd[r][c] == 0: continue

            bd[r][c] += min(bd[r][c - 1], bd[r - 1][c], bd[r - 1][c - 1])

    mxv = max([max(ln) for ln in bd])
    print(mxv ** 2)
