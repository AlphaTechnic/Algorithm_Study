import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

SZ = 10000001


def cnt_primelike(p, L, R):
    cnt = 0
    num = p ** 2
    while num < L:
        num *= p
    while num <= R:
        cnt += 1
        R = num * p
    return cnt


if __name__ == "__main__":
    is_prime = [True for _ in range(SZ)]
    for i in range(2, SZ):
        for j in range(i + i, SZ, i):
            if not is_prime[i]: continue

            is_prime[j] = False

    primes = []
    for i in range(2, SZ):
        if is_prime[i]:
            primes.append(i)

    L, R = map(int, input().rstrip().split())
    cnt = 0
    for i in range(len(primes)):
        if primes[i] ** 2 > R:
            break

        cnt += cnt_primelike(primes[i], L, R)
    print(cnt)
