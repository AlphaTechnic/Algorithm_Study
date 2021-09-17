"""
input :
45

output :
24
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
MAX = 10 ** 6


def get_factors(N):
    facts = set()
    for i in range(len(primes)):
        while N % primes[i] == 0:
            facts.add(primes[i])
            N //= primes[i]

    if N != 1:
        facts.add(N)

    return list(facts)


if __name__ == "__main__":
    # 소수 전처리
    is_prime = [True for _ in range(MAX + 1)]
    for i in range(2, MAX + 1):
        for j in range(i + i, MAX + 1, i):
            if is_prime[j] is False: continue
            is_prime[j] = False

    primes = []
    for i in range(2, len(is_prime)):
        if is_prime[i]:
            primes.append(i)

    N = int(input())
    facts = get_factors(N)

    fact_mul = 1
    for fact in facts:
        fact_mul *= fact
    tmp = 1
    for fact in facts:
        tmp *= (fact - 1)
    print(tmp * (N // fact_mul))
