import sys
sys.stdin = open("input.txt", "r")

N, M, K = map(int, input().split())

change = []
for i in range(M):
    tmp = list(map(int, input().split()))
    change.append(tmp)

par = [[0]*30 for _ in range(N+1)]
for i in range(1, N+1):
    t = i
    for lr in change:
        if (lr[0] <= t <= lr[1]) is False:
            continue
        t = lr[1] - (t - lr[0])
    par[t][0] = i

for j in range(1, 30):
    for i in range(1, N+1):
        par[i][j] = par[par[i][j-1]][j-1]

ans = [0 for _ in range(N+1)]
for i in range(1, N+1):
    c = K
    ind = 0
    res = i
    while c:
        if c % 2:
            res = par[res][ind]
        c //= 2
        ind += 1
    ans[i] = res

for i in range(1, N+1):
    print(ans[i])