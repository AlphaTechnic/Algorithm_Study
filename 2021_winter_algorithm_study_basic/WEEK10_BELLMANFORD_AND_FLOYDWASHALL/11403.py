import sys
sys.stdin = open("input.txt", "r")

graph = [[0 for _ in range(101)] for _ in range(101)]

def get_connection():
    for k in range(1, N+1):
        for i in range(1, N+1):
            if graph[i][k] == 0:
                continue
            for j in range(1, N+1):
                if graph[k][j] == 0:
                    continue
                graph[i][j] = 1

N = int(input())
for i in range(1, N+1):
    row = list(map(int, input().split()))
    for j in range(1, N+1):
        graph[i][j] = row[j-1]


get_connection()

for i in range(1, N+1):
    for j in range(1, N+1):
        print(graph[i][j], end=' ')
    print()



