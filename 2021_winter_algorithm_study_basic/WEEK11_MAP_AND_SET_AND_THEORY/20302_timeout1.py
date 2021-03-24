import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def is_divided(N, M):
    if N % M == 0:
        return True
    else:
        return False


def gcd(N, M):
    if M == 0:
        return N
    return gcd(M, N % M)


def short_fraction(N, M):  # 기약분수
    a = N // gcd(N, M)
    b = M // gcd(N, M)
    return a, b


N = int(input())
oper_list = input().split()
upper = 1
lower = 1
upper *= int(oper_list[0])

for ind, operator_or_operand in enumerate(oper_list[1:]):
    if ind % 2 == 0:  # 연산자
        operator = operator_or_operand
    else:  # 피연산자
        if operator == '*':
            upper *= int(operator_or_operand)
        else:  # '/'
            lower *= int(operator_or_operand)
    upper, lower = short_fraction(upper, lower)

if is_divided(upper, lower):
    print("mint chocolate")
else:
    print("toothpaste")
