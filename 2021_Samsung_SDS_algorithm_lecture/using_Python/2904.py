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

N = int(input())
nums = list(map(int, input().rstrip().split()))

################# 소수에 대한 전처리
is_composite = [False for _ in range(1001)]
for i in range(2, 1001):
    if is_composite[i]:
        continue
    for j in range(i + i, 1001, i):
        is_composite[j] = True

primes = []
for i in range(2, 1001):
    if not is_composite[i]:
        primes.append(i)
###################################

factorization_board = []  # 각 factorization_board에 인수분해 결과 기록
master_board = dict()  # 제시된 수들에 등장한 factor들을 종합하여 기록
"""
예시 : 1 100 100
factorization_board = [{2: 0, 5: 0}, {2: 2, 5: 2}, {2: 2, 5: 2}]
master_board = {2: 4, 5: 4}
"""


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
        master_board[num] = 1

    factorization_board.append(factor_dic)


for i, num in enumerate(nums):
    factorize(num)

# 해당 number가 가지고 있지 않는 factor 개수에 대해 0을 주는 작업
for factor in master_board.keys():
    for factorization in factorization_board:
        if factor not in factorization:
            factorization[factor] = 0

"""
인자로 주어진 factor들을 balance 있게 분배하는 함수

- balance_split(2, 4) 예시 - 주어진 숫자 1 100 100 에서 2가 4개 있다는 의미
side effect : balance_division = [2, 1, 1]
return : 2^1
"""
def balance_split(factor, cnt):
    global N
    q = cnt // N
    r = cnt % N

    for i in range(N):
        if r > 0:
            balance_division[i] += q + 1
            r -= 1
        else:
            balance_division[i] += q

    return factor ** q


move_num = 0
max_val = 1
for factor in master_board.keys():
    tot = 0
    if master_board[factor] >= N:
        balance_division = [0 for _ in range(N)]
        max_val *= balance_split(factor, master_board[factor])

        factor_num = []
        for i in range(N):
            factor_num.append(factorization_board[i][factor])
        factor_num.sort(reverse=True)

        """
        balance_division = [2, 1, 1] 과 factor_num = [2, 2, 0] 의 차이를 이용
        """
        for i in range(N):
            # factor 부족한 애들이라면, 얼마나 더 채워줘야되는가
            tot += max(0, balance_division[i] - factor_num[i])
    move_num += tot

print(max_val, move_num)