"""
input :
3
8 24 9

output :
12 3
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

primes = []
factorization_board = []  # 각 factorization_board에 인수분해 결과 기록
master_board = dict()  # 제시된 수들에 등장한 factor들을 종합하여 기록


def gen_primes():
    is_composite = [False for _ in range(1001)]
    for i in range(2, 1001):
        if is_composite[i]:
            continue
        for j in range(i + i, 1001, i):
            is_composite[j] = True

    for i in range(2, 1001):
        if not is_composite[i]:
            primes.append(i)


def factorize(num):
    factor_dic = dict()
    for p in primes:
        if num % p == 0:
            while True:
                if p not in factor_dic:
                    factor_dic[p] = 1
                else:
                    factor_dic[p] += 1

                if p not in master_board:
                    master_board[p] = 1
                else:
                    master_board[p] += 1

                num //= p
                if num % p != 0:
                    break

    if num > 1:
        factor_dic[num] = 1
        # 다른 수에서 먼저 추가했을 수 있으므로 += 1
        if num not in master_board:
            master_board[num] = 1
        else:
            master_board[num] += 1

    factorization_board.append(factor_dic)


if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().rstrip().split()))

    gen_primes()

    for i, num in enumerate(nums):
        factorize(num)

    # 해당 number가 가지고 있지 않는 factor 개수에 대해 0을 주는 작업
    for factor in master_board.keys():
        for factorization in factorization_board:
            if factor not in factorization:
                factorization[factor] = 0

    move_num = 0
    gcd = 1
    for factor in master_board.keys():
        tot = 0
        if master_board[factor] >= N:
            q = master_board[factor] // N

            gcd *= factor ** q

            for i in range(N):
                tot += max(0, q - factorization_board[i][factor])

        move_num += tot

    print(gcd, move_num)


