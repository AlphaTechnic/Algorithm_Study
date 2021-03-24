import sys
sys.stdin = open("input.txt", "r")


def find_min_in_2Darr():
    Min = int(1e9)
    for i in range(1, N+1):
        tmp = sum(arr[i])
        if Min > tmp:
            Min = tmp
            ind = i
    return ind


def floydwashall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            if k == i:
                continue
            if arr[i][k] == 0:
                continue
            for j in range(1, N+1):
                if k == j or i ==j:
                    continue
                if arr[k][j] == 0:
                    continue
                if arr[i][j] == 0 or arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]


N, M = map(int, input().split())
arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    arr[a][b] = arr[b][a] = 1

floydwashall()
print(find_min_in_2Darr())

