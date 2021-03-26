import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

cnt = 0
N, M = map(int, input().split())
N = N - M
cnt += 1
if N % (M - 1) == 0:
    cnt += N // (M - 1)
else:
    cnt += N // (M - 1) + 1

print(cnt)
