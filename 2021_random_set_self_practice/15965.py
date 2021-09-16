"""
input :
3

output :
5
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 7368788

if __name__ == "__main__":
    N = int(input())
    if N == 1:
        print(2)
        exit(0)

    isprime = [True for _ in range(MAX)]
    for i in range(2, len(isprime)):
        for j in range(i + i, len(isprime), i):
            if not isprime[i]: continue
            isprime[j] = False

    ind = 1
    for num in range(3, MAX, 2):
        if isprime[num]:
            ind += 1
            if ind == N:
                print(num)
