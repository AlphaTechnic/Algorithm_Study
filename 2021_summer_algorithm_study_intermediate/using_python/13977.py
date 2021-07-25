"""
input :
5
5 2
5 3
10 5
20 10
10 0

output :
10
10
252
184756
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def power(a, b):
    if b == 0:
        return 1
    if b % 2:  # 홀수이면
        return ((power(a, b // 2) ** 2) * a) % p
    else:
        return (power(a, b // 2) ** 2) % p


if __name__ == "__main__":
    p = 1000000007
    Q = int(input())

    # factorial 전처리
    fact = [1 for _ in range(4000001)]
    for i in range(2, 4000001):
        fact[i] = (fact[i - 1] * (i % p)) % p

    for _ in range(Q):
        N, K = map(int, input().split())

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
