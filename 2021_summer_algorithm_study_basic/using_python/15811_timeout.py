"""
input :
SUN FUN SWIM

output :
YES
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def calculate(string):
    scale = 1
    tot = 0
    for i in range(len(string) - 1, -1, -1):
        tot += to_int[string[i]] * scale
        scale *= 10
    return tot


def correct_res():
    return calculate(str_c) == calculate(str_a) + calculate(str_b)


def recur(dep):
    if dep == LIMIT:
        if correct_res():
            print("YES"); exit()
        return

    for i in range(10):
        if isused[i]: continue

        to_int[chars[dep]] = i
        isused[i] = True

        recur(dep + 1)

        to_int[chars[dep]] = '_'
        isused[i] = False


if __name__ == "__main__":
    str_a, str_b, str_c = input().rstrip().split()
    chars = list(set(str_a) | set(str_b) | set(str_c))

    LIMIT = len(chars)
    to_int = dict()
    isused = [False for _ in range(10)]
    recur(0)
    print("NO")
