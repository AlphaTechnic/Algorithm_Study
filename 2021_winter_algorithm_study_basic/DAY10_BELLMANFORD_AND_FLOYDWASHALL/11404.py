import sys
sys.stdin = open("input.txt", "r")

INF = int(1e9)


def floydwashall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]


N = int(input())
M = int(input())
arr = [[INF for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            arr[i][j] = 0

for i in range(M):
    a, b, w = map(int, input().split())
    if arr[a][b] == INF:
        arr[a][b] = w
    elif arr[a][b] > w:
        arr[a][b] = w

floydwashall()

for i in range(1, N+1):
    for j in range(1, N+1):
        if arr[i][j] == INF:
            print(0, end= ' ')
        else:
            print(arr[i][j], end=' ')
    print()

