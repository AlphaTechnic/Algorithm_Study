import sys

sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
mat = []
for i in range(N):
    mat.append(input())

ans = 64
for i in range(0, M-7):
    for j in range(0, N-7):
        case1 = 0
        case2 = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if mat[b][a] == 'W':
                    if (a + b) % 2 == 1:
                        case1 += 1
                    else:
                        case2 += 1
                else:
                    if (a + b) % 2 == 1:
                        case2 += 1
                    else:
                        case1 += 1

        ans = min(case1, case2, ans)

print(ans)