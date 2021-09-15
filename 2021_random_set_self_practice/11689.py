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
    while N != 1:
        facts.add(least_prime_factor[N])
        N = N // least_prime_factor[N]
    return list(facts)


if __name__ == "__main__":
    least_prime_factor = [i for i in range(MAX + 1)]
    for i in range(2, MAX + 1):
        for j in range(i + i, MAX + 1, i):
            if least_prime_factor[j] != j: continue
            least_prime_factor[j] = i

    N = int(input())
    facts = get_factors(N)

    fact_mul = 1
    for fact in facts:
        fact_mul *= fact
    tmp = 1
    for fact in facts:
        tmp *= (fact - 1)
    print(tmp * (N // fact_mul))






