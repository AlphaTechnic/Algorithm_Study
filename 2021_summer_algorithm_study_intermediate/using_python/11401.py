"""
input :
5 2

output :
10
"""

import sys
sys.stdin = open("input.txt", "r")
read = sys.stdin.readline


def power(a, b):
    if b == 0:
        return 1
    if b % 2:  # 홀수이면
        return ((power(a, b // 2) ** 2) * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


if __name__ == "__main__":
    p = 1000000007
    N, K = map(int, read().split())

    fact = [1 for _ in range(N+1)]

    for i in range(2, N+1):
        fact[i] = (fact[i - 1] * (i % p)) % p

    A = fact[N]
    B = (fact[N-K] * fact[K]) % p

    """
    페르마의 소정리
    (A/B) % p
    = A * B^-1 % p
    = A * B^-1 * B^p-1 % p
    = A * B^p-2 % p
    = (A % p) * (B^p-2 % p) % p
    """
    print((A * power(B, p-2)) % p)
