import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

# 에라토스테네스의 체
# chk = ['_', '_'] + [True for _ in range(2, 101)]
#
# for i in range(2, 101):
#     for j in range(i + i, 101, i):
#         if chk[j]:
#             chk[j] = False
#
# primes = []
# for i in range(2, 101):
#     if chk[i]:
#         primes.append([i, 0])

MAX = 100000
nums = [0 for _ in range(MAX + 1)]


def stack_factors(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            while num % i == 0:
                num //= i
                nums[i] += 1
    if num > 1:
        nums[num] += 1


def pop_factors(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            while num % i == 0:
                num //= i
                nums[i] -= 1
    if num > 1:
        nums[num] -= 1


def main():
    N = int(input())

    expr = input().split()
    if int(expr[0]) == 0:
        print("mint chocolate")
        return
    stack_factors(abs(int(expr[0])))

    for i in range(1, len(expr), 2):
        if expr[i] == '*':
            if int(expr[i + 1]) != 0:
                stack_factors(abs(int(expr[i + 1])))
            else:
                print("mint chocolate")
                return
        else:
            pop_factors(abs(int(expr[i + 1])))

    for num in nums:
        if num < 0:
            print("toothpaste")
            return
    print("mint chocolate")
    return


main()
