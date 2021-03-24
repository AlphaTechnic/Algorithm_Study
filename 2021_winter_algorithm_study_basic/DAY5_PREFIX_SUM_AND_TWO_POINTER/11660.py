import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split()) # 표의 크기 N과 합을 구해야 하는 횟수 M
num_table = [[0]*(N+1)]
start_end_coordi = []

for _ in range(N):
    num_table.append([0] + list(map(int, input().split())))
for _ in range(M):
    start_end_coordi.append(list(map(int, input().split())))
pre = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, N+1):
       pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + num_table[i][j]

for start_r, start_c, end_r, end_c in start_end_coordi:
    print(pre[end_r][end_c] - (pre[end_r][start_c - 1] + pre[start_r - 1][end_c] - pre[start_r - 1][start_c - 1]))
