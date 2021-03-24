import sys

sys.stdin = open("input.txt", "r")

N = int(input())
levels = list(map(int, input().split()))
levels_sorted = sorted(levels)

Min = 200000
for i in range(N):
    candi = levels_sorted[i] + levels_sorted[2*N-i-1]
    if candi < Min:
        Min = candi

print(Min)
