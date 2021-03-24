import sys

sys.stdin = open("input.txt", "r")

N = int(input())
inward = dict()
order = 0
for _ in range(N):
    inward[input()] = order
    order += 1

outward = list()
for _ in range(N):
    key = input()
    outward.append((key, inward[key]))

cnt = 0
for i in range(N):
    for j in range(i + 1, N):
        if outward[i][1] > outward[j][1]:
            cnt += 1
            break

print(cnt)
