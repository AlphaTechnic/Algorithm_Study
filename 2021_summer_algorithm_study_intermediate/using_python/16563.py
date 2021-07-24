"""
input :
5
5 4 45 64 54

output :
5
2 2
3 3 5
2 2 2 2 2 2
2 3 3 3
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def factorize(num):
    while True:
        if least_primes[num] == -1:
            print(num, end=' ')
            break
        print(least_primes[num], end=' ')
        num //= least_primes[num]


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    # 전처리
    # sqrt(5,000,000) < 2240
    primes = []
    least_primes = [-1 for _ in range(5000001)]
    for i in range(2, 2240):
        for j in range(i + i, 5000001, i):
            if least_primes[j] != -1: continue

            least_primes[j] = i
    ##########################################

    for num in nums:
        factorize(num)
        print()
