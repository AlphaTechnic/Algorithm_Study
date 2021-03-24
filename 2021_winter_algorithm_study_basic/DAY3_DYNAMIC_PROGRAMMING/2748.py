import sys

sys.stdin = open("input.txt", "r")

n = int(input())
fibo_list = [-1 for _ in range(100)]


def fibo(n):
    if fibo_list[n] != -1: # 수열 정보가 fibo_list에 저장되어 있다면
        return fibo_list[n]

    if n == 0:
        fibo_list[n] = 0
        return fibo_list[n]
    elif n == 1:
        fibo_list[n] = 1
        return fibo_list[n]

    if fibo_list[n] == -1:
        fibo_list[n] = fibo(n-2) + fibo(n-1)
        return fibo_list[n]

print(fibo(n))